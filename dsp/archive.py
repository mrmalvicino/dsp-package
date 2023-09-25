import os
import datetime


class Archive:

    def __init__(self, save_kwargs = None, save_figure_kwargs = None):
        if save_kwargs is None:
            save_kwargs = {'output_path': os.path.realpath(os.path.join(self.get_root_dir(), '..', 'output')), 'file_name': str(datetime.datetime.now()) + ' by ' + os.getlogin()}

        self._save_kwargs = save_kwargs

        if save_figure_kwargs is None:
            save_figure_kwargs = {'bbox_inches': 'tight', 'dpi': 300, 'transparent': False}

        self._save_figure_kwargs = save_figure_kwargs


    @property
    def save_kwargs(self):
        return self._save_kwargs

    @save_kwargs.setter
    def save_kwargs(self, save_kwargs):
        self._save_kwargs = save_kwargs

    @property
    def save_figure_kwargs(self):
        return self._save_figure_kwargs

    @save_figure_kwargs.setter
    def save_figure_kwargs(self, save_figure_kwargs):
        self._save_figure_kwargs = save_figure_kwargs


    def get_root_dir(self, is_ipynb = False):
        if is_ipynb == True:
            root_dir = os.getcwd()
        else:
            root_dir = os.path.dirname(__file__)

        return root_dir


    def save_plot(self, graph):
        save_path = os.path.join(self.save_kwargs['output_path'], self.save_kwargs['file_name'] + '.png')
        graph.savefig(save_path, ** self.save_figure_kwargs)

        return


    def save_array(self, array):
        """
        Saves a given numpy array into a file at the hard drive.

        Args:
            array (numpy.ndarray) Data that is going to be saved.

        Returns:
            None
        """

        np.save(os.path.join(self.save_kwargs['output_path'], self.save_kwargs['file_name']), array)

        return