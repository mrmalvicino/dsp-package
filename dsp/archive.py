import numpy as np
import os
import datetime


class Archive:

    def __init__(self):
        self._resources_path = os.path.realpath(os.path.join(self.get_root_dir(), '..', 'resources'))
        self._output_path = os.path.realpath(os.path.join(self.get_root_dir(), '..', 'output'))
        self._save_figure_kwargs = {'bbox_inches': 'tight', 'dpi': 300, 'transparent': True}


#######################
## GETTERS & SETTERS ##
#######################


    @property
    def resources_path(self):
        return self._resources_path

    @resources_path.setter
    def resources_path(self, resources_path):
        self._resources_path = resources_path

    @property
    def output_path(self):
        return self._output_path

    @output_path.setter
    def output_path(self, output_path):
        self._output_path = output_path

    @property
    def save_figure_kwargs(self):
        return self._save_figure_kwargs

    @save_figure_kwargs.setter
    def save_figure_kwargs(self, save_figure_kwargs):
        self._save_figure_kwargs = save_figure_kwargs


#############
## METHODS ##
#############


    def get_root_dir(self, is_ipynb = False):
        if is_ipynb == True:
            root_dir = os.getcwd()
        else:
            root_dir = os.path.dirname(__file__)

        return root_dir


    def save_plot(self, graph, file_name = None):
        if file_name is None:
            file_name = str(datetime.datetime.now()) + ' by ' + os.getlogin()

        file_path = os.path.join(self.output_path, file_name + '.png')
        graph.savefig(file_path, **self.save_figure_kwargs)

        return


    def save_array(self, array):
        """
        Saves a given numpy array into a file at the hard drive.

        Args:
            array (numpy.ndarray) Data that is going to be saved.

        Returns:
            None
        """

        file_path = os.path.join(self.output_path, self.file_name)
        np.save(file_path, array)

        return