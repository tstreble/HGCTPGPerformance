
from rootpy.plotting import get_style
import copy

style_turnon = copy.deepcopy(get_style('CMSTDR'))
style_turnon.SetName('Turnon')
style_turnon.SetPadRightMargin(0.04)
style_turnon.SetLabelSize(0.05, 'XY')
style_turnon.SetTitleSize(0.06, 'XY')
style_turnon.SetTitleXOffset(0.95)
style_turnon.SetTitleYOffset(1.1)

style_rate = copy.deepcopy(get_style('CMSTDR'))
style_rate.SetName('Rate')
style_rate.SetPadRightMargin(0.04)
style_rate.SetLabelSize(0.05, 'XY')
style_rate.SetTitleSize(0.06, 'XY')
style_rate.SetTitleXOffset(0.95)
style_rate.SetTitleYOffset(1.1)
