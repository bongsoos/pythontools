'''
plottools.py

Plotting tools

Tools
-----
    makefig
    set_axis
    simpleaxis
    get_color
    set_label
    savefig

author: Bongsoo Suh
created: 2015-09-01

(C) 2015 bongsoos
'''

import numpy as _np
from matplotlib import pyplot as _plt
from mpl_toolkits.axes_grid1 import make_axes_locatable as _mal
import matplotlib.patches as _mpatches
import matplotlib.colors as _colors
import matplotlib.cm as _cmx
import matplotlib as mpl

NCURVES = 10
_np.random.seed(101)
curves = [_np.random.random(20) for i in range(NCURVES)]
values = range(NCURVES)

def get_color(cmap, idx):
    '''
    get color
    '''
    colormap = _plt.get_cmap(cmap)
    cNorm  = _colors.Normalize(vmin=0, vmax=values[-1])
    scalarMap = _cmx.ScalarMappable(norm=cNorm, cmap=colormap)
    colorVal = scalarMap.to_rgba(values[idx])
    print(scalarMap.get_clim())

    return colorVal


def simpleaxis(ax):
    '''
    simple axis
    '''
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()


def set_axis(ax, ax_disp=['left','bottom'], x_ticks=None, x_ticks_label=None, y_ticks=None, y_ticks_label=None,
             lbsize=12, islabel=True, ax_linewidth=0.8, ax_tickwidth=0.8, xlim=None, ylim=None, islog_x=False, islog_y=False):
    '''
    Axis setup.

    Usage
    -----
        set_axis(ax, x_ticks=[0, 1], y_ticks=[0, 2])
        set_axis(ax, x_ticks=[0, 1], y_ticks=[0, 2], islabel=False) # this will not display axis labels
        set_axis(ax, x_ticks=[0, 1], y_ticks=[0, 2], xlim=[0,5], ylim=[0,1]) # this will not display axis labels

    Inputs
    ------
        ax (object):
            Pass the figure axis object.

        ax_disp (list):
            Choose axis that you want to display. 'top', 'right' 'left','bottom'
            Default = ['left', 'bottom']

        x_ticks (list):
            x tick location. ex) [-1, 0, 1]

        y_ticks (list):
            y tick location. ex) [-1, 0, 1]

        x_ticks_label (list):
            x tick label. ex) [-1, 0, 1]

        y_ticks_label (list):
            y tick label. ex) [-1, 0, 1]

        lbsize (int):
            label size (default = 20)

        islabel (bool):
            Select to display the axis labels(True) or not(False).

        ax_linewidth (int):
            axis line width (default = 2)

        ax_tickwidth (int):
            axis tick width (default = 2)

        xlim (list):
            x axis range. ex) [-1, 1]

        ylim (list):
            y axis range. ex) [0, 1]

        islog_x (bool):
            set x axis into log scale

        islog_y (bool):
            set y axis into log scale
    '''
    # set axis
    all_axes = ['top','right','left','bottom']
    for d in all_axes:
        if d not in ax_disp:
            ax.spines[d].set_visible(False)
    for d in ax_disp:
        ax.spines[d].set_linewidth(ax_linewidth)

    # set ticks
    # axis: changes apply to 'x' or 'y' axis
    # which: 'both'. both major and minor ticks are affected
    # top, bottom, left, right: 'off'. ticks along the axis edges are off
    # labelbottom, labelright: 'off'. turn off the label
    if ['top','right'] not in ax_disp:
        ax.tick_params(axis='x', which='both', top='off', labelsize=lbsize, width=ax_tickwidth)
        ax.tick_params(axis='y', which='both', right='off', labelright='off', labelsize=lbsize, width=ax_tickwidth)

    # set tick labels
    if x_ticks is not None:
        ax.set_xticks(x_ticks)
    if y_ticks is not None:
        ax.set_yticks(y_ticks)
    if x_ticks_label is not None:
        ax.set_xticklabels(x_ticks_label)
    if y_ticks_label is not None:
        ax.set_yticklabels(y_ticks_label)

    if not islabel:
        ax.tick_params(labelbottom='off',labelleft='off')

    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)

    if islog_x:
        ax.set_xscale('log')
    if islog_y:
        ax.set_yscale('log')

    return


def set_label(ax, title=' ', x_label=' ', y_label=' ', ftsize=12, title_ftsize=None, title_offset=1.05, islabel=True):
    '''
    Set labels

    Inputs
    ------
        ax (object):
            axis object

        title (string)
        x_label (string)
        y_label (string)
        ftsize (int):
            font size for title, x_label, y_label. Default = 20

        lbsize (int):
            label size for axis. Default = 20
    '''
    if islabel:
        if title_ftsize is None:
            ax.set_title(title, fontsize=ftsize, y=title_offset)
        else:
            ax.set_title(title, fontsize=title_ftsize, y=title_offset)

        ax.set_xlabel(x_label, fontsize=ftsize)
        ax.set_ylabel(y_label, fontsize=ftsize)

    return


# fig_class
def makefig(figsize=(5,5), num_plots=1, dpi=500):
    '''
    Make figure
    Usage
    -----
        makefig()
        makefig(figsize=(3,3))

    Inputs
    ------
        figsize (tuple):
            figure size (width, height)
            ex) (3,3)

        num_plots (int):
            number of plots(subplots) in the figure. Default = 1

        title (string):
        x_label (string):
        y_label (string):

    Outputs
    -------
        fig (object):
            figure object

        ax (object, dictionary):
            axis object[dictionary].
            For num_plots=1 case, returns one ax object.
            For num_plots>1 case, returns dictionary. Axes can be accessed using the key values
            starting from 0 to num_plots-1. ex) ax[0]~ax[num_plots-1].
    '''
    fig = _plt.figure(figsize=figsize, dpi=dpi)
    if num_plots == 1:
        ax = fig.add_subplot(111)
        # fig.tight_layout()
    else:

        ### figure subplot grid (row = x, col = y)
        plotsize_x = _np.int(_np.ceil(num_plots/3))
        plotsize_y = _np.int(_np.ceil(num_plots/plotsize_x))

        figsize_x = figsize[1]
        figsize_y = figsize[0]
        fig = _plt.figure(figsize=(plotsize_y*figsize_y, plotsize_x*figsize_x))
        ax = {}

        for i in range(num_plots):
            ax[i] = fig.add_subplot(plotsize_x, plotsize_y, i+1)

        fig.tight_layout()

    # return fig, ax objects
    return fig, ax


def savefig(fig, filename=None, dpi=500, tight=True):
    '''
    save figure

    Usage
    -----
        savefig(fig, 'fig1') # this will save fig into fig1.png file.

    Inputs
    ------
        fig (object):
            figure object created using makefig or matplotlib pyplot.

        filename (string):
            file name that figure will be saved.
    '''
    if tight:
        fig.tight_layout()
    if filename is not None:
        fig.savefig(filename, bbox_inches='tight', dpi=dpi)
    else:
        print("File name must be given. Usage: ex) savefig(fig, 'fig1')" )

    return

