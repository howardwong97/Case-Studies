import matplotlib.pyplot as plt
import seaborn as sns

CB91_Blue = '#2CBDFE'
CB91_Green = '#47DBCD'
CB91_Pink = '#F3A0F2'
CB91_Purple = '#9D2EC5'
CB91_Violet = '#661D98'
CB91_Amber = '#F5B14C'

color_list = [CB91_Blue, CB91_Pink, CB91_Green, CB91_Amber,
              CB91_Purple, CB91_Violet]
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)
plt.style.use('seaborn')

CB91_Grad_BP = ['#2cbdfe', '#2fb9fc', '#33b4fa', '#36b0f8',
                '#3aacf6', '#3da8f4', '#41a3f2', '#449ff0',
                '#489bee', '#4b97ec', '#4f92ea', '#528ee8',
                '#568ae6', '#5986e4', '#5c81e2', '#607de0',
                '#6379de', '#6775dc', '#6a70da', '#6e6cd8',
                '#7168d7', '#7564d5', '#785fd3', '#7c5bd1',
                '#7f57cf', '#8353cd', '#864ecb', '#894ac9',
                '#8d46c7', '#9042c5', '#943dc3', '#9739c1',
                '#9b35bf', '#9e31bd', '#a22cbb', '#a528b9',
                '#a924b7', '#ac20b5', '#b01bb3', '#b317b1']

sns.set(font='DejaVu Sans', rc={
        'axes.axisbelow': False,
        'axes.edgecolor': 'black',
        'axes.facecolor': 'None',
        'axes.grid': False,
        'axes.labelcolor': 'black',
        'axes.spines.right': False,
        'axes.spines.top': False,
        'figure.facecolor': 'white',
        'lines.solid_capstyle': 'round',
        'patch.edgecolor': 'w',
        'patch.force_edgecolor': True,
        'text.color': 'black',
        'xtick.bottom': False,
        'xtick.color': 'black',
        'xtick.direction': 'out',
        'xtick.top': False,
        'ytick.color': 'black',
        'ytick.direction': 'out',
        'ytick.left': False,
        'ytick.right': False
    })

sns.set_context("notebook", rc={"font.size": 12, "axes.titlesize": 16, "axes.labelsize": 12})