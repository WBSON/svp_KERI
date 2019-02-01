
import os
import sys
import das
import time
import dataset
import multiprocessing
import traceback
import script

print sys
print sys.path

default_data_points = {
    'time': 0,
    'dc_voltage': 380,
    'dc_current': 10,
    'ac_voltage': 240,
    'ac_current': 14,
    'dc_watts': 3800,
    'ac_va': 3360,
    'ac_watts': 3200,
    'ac_vars': 160,
    'ac_freq': 60.0,
    'ac_pf': .952,
    'trigger': 0,
    'ametek_trigger': 0
}

data_points = [
    'time',
    'dc_voltage',
    'dc_current',
    'ac_voltage',
    'ac_current',
    'dc_watts',
    'ac_va',
    'ac_watts',
    'ac_vars',
    'ac_freq',
    'ac_pf',
    'trigger',
    'ametek_trigger'
]


class DataProcess(object):

    def __init__(self, params, data_conn, data_err_conn, interval=1):
        self.params = params
        self.data_conn = data_conn
        self.data_err_conn = data_err_conn
        self.active = True
        self.capture = False
        self.interval = interval
        self.error_msg = None
        self.rec = {}
        self.recs = []

    def error(self, error_msg):
        if self.error_msg is None:
            self.error_msg = error_msg
            self.data_err_conn.send(error_msg)

    def conn_msg(self):
        msg = None
        try:
            if self.data_conn:
                if self.data_conn.poll():
                    msg = self.data_conn.recv()
        except Exception, e:
            self.error(traceback.format_exc())

        return msg

    def sleep(self, seconds):
        try:
            t = time.time()
            expire = t + seconds
            while (t < expire):
                msg = self.conn_msg()
                if msg is not None:
                    if msg == 'start':
                        self.recs = []
                        self.capture = True
                    elif msg == 'stop':
                        self.capture = False
                    elif msg == 'dataset':
                        if self.capture is False:
                            self.data_conn.send(self.recs)
                    elif msg == 'data':
                        self.data_conn.send(self.rec)
                    elif msg == 'quit':
                        self.active = False
                    elif msg == 'name':
                        self.data_conn.send(multiprocessing.current_process().name)
                    elif msg == 'error':
                        self.data_conn.send(self.error_msg)
                    elif msg == 'info':
                        self.data_conn.send(str(self.params))
                else:
                    time.sleep(.01)
                t = time.time()
        except Exception, e:
            self.error(traceback.format_exc())

    def run(self):
        try:
            while self.active:
                if self.error_msg is None:
                    self.rec = dict(default_data_points)
                    self.rec['time'] = time.time()
                    if self.capture:
                        self.recs.append(self.rec)
                self.sleep(self.interval)
        except Exception, e:
            self.error(traceback.format_exc())


def data_process(params, data_conn, data_err_conn, interval):
    process = DataProcess(params, data_conn, data_err_conn, interval)
    process.run()


class Data(object):

    def __init__(self, ts, params=None, capture_interval=.1, data_file=None, capture_files=None):
        self.params = params
        self.data_file = data_file
        self.capture_files = capture_files
        self.capture_file_index = 0
        self.data_dataset = None
        self.data_dataset_last = 0
        # self.capture_dataset = None
        self.capture_interval = capture_interval
        self.capture_start_time = None
        self.capture_stop_time = None
        self.capture_enabled = False
        if self.capture_files is None:
            self.capture_files = []

        self.data_conn, self.conn = multiprocessing.Pipe()
        self.data_err_conn, self.err_conn = multiprocessing.Pipe()
        self.process = None
        self.process_start(params=self.params)

        # if self.data_file is not None:
        #     ts.log('data file = %s' % self.data_file)

    def cmd(self, cmd_str):
        resp = None
        if self.process and self.conn:
            self.conn.send(cmd_str)
            # self.ts.log('sending process cmd: %s' % (cmd_str))
            count = 0
            while count < 100:
                if self.conn.poll():
                    # self.ts.log('receiving process cmd: %s' % (cmd_str))
                    resp = self.conn.recv()
                    count = 100
                else:
                    time.sleep(.01)
                    count += 1
        else:
            raise das.DASError('Error sending process command: %s' % (cmd_str))

        return resp

    def process_start(self, params=None):
        if self.process is None:
            # self.process = MultiProcess(target=data_process, args=(params, self.data_conn, self.data_err_conn,
            #                                                        self.capture_interval))
            self.process = script.Process(target=data_process, args=(params, self.data_conn, self.data_err_conn,
                                                                     self.capture_interval))
            self.process.start()
            # self.ts.log('starting process %s' % (self.process))
            self.process_error_check()

    def process_error_check(self):
        if self.err_conn.poll():
            err_msg = self.err_conn.recv()
            raise das.DASError('Data process error: %s' % (err_msg))

    def capture_start(self):
        self.capture_start_time = time.time()
        self.capture_enabled = True
        if self.process and self.conn:
            self.conn.send('start')
        else:
            raise das.DASError('Error starting data capture')
        self.process_error_check()

    def capture_stop(self):
        self.capture_stop_time = time.time()
        self.capture_enabled = False
        if self.process and self.conn:
            self.conn.send('stop')
        else:
            raise das.DASError('Error stopping data capture')
        self.process_error_check()

    def capture(self):
        return self.capture_enabled

    def capture_dataset(self):
        ds = dataset.DataSet(points=data_points)
        if not self.capture_enabled:
            ds.recs = self.cmd('dataset')
        self.process_error_check()
        return ds

    def read(self):
        data = self.cmd('data')
        self.process_error_check()
        return data

    def info(self, time=None):
        name_str = self.cmd('info')
        self.process_error_check()
        return name_str

    def __str__(self):
        '''
        s = 'dsm_data:\n'
        for k, v in dsm_points.iteritems():
            s += '  %s: %s\n' % (v, self[v])
        return s
        '''
        pass


if __name__ == "__main__":

    pass


