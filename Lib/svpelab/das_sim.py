
import sys
import os
import das
import time
import dataset
import data_sim
import multiprocessing
import script

sim_info = {
    'name': os.path.splitext(os.path.basename(__file__))[0],
    'mode': 'DAS Simulation'
}

def das_info():
    return sim_info

def params(info, group_name=None):
    gname = lambda name: group_name + '.' + name
    pname = lambda name: group_name + '.' + GROUP_NAME + '.' + name
    mode = sim_info['mode']
    info.param_add_value(gname('mode'), mode)
    info.param_group(gname(GROUP_NAME), label='%s Parameters' % mode,
                     active=gname('mode'),  active_value=mode, glob=True)
    info.param(pname('data_file'), label='Data File', default='data.csv', ptype=script.PTYPE_FILE)


GROUP_NAME = 'sim'


class DAS(das.DAS):
    """
    Template for data acquisition implementations. This class can be used as a base class or
    independent data acquisition classes can be created containing the methods contained in this class.
    """

    def __init__(self, ts, group_name):
        das.DAS.__init__(self, ts, group_name)
        self.data_file = self._param_value('data_file')
        self.data = None
        self.params = {}

        self.data = self._data_init()
        self.trigger_enabled = False

    def _param_value(self, name):
        return self.ts.param_value(self.group_name + '.' + GROUP_NAME + '.' + name)

    def _data_init(self):
        if self.data is None:
            self.data = data_sim.Data(self.ts, params=self.params, data_file=self.data_file)
        # self.data.process_start()
        return self.data

    def close(self):
        """
        Close any open communications resources associated with the data module.
        """
        if self.data is not None and self.data.process is not None:
            try:
                self.data.process.terminate()
                self.data.process.join()
            except Exception, e:
                raise

    def data_capture(self, capture=None):
        if self.data is not None:
            if capture is not None:
                if capture is True:
                    self.data.capture_start()
                else:
                    self.data.capture_stop()
        else:
            raise das.DASError('Data initialization error')
        return self.data.capture()

    def data_capture_dataset(self):
        if self.data is not None:
            ds = self.data.capture_dataset()
        else:
            raise das.DASError('Data initialization error')
        return ds

    def data_read(self):
        if self.data is not None:
            data = self.data.read()
        else:
            raise das.DASError('Data initialization error')
        return data

    def trigger(self, enabled=None):
        if enabled is not None:
            self.trigger_enabled = enabled
        return self.trigger_enabled


if __name__ == "__main__":

    pass


