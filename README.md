labreporthelper
===============

Module in python to help in automating lab reports

Installations
-------------
Clone and run
```
python setup.py install
```

Usage
-----
Create base python files using

```
make-lab-report
```

Control using manage.py


Change Log
==========

0.2
---
- Add CurveFit (wrapper for scipy.optimize.curvefit) to labreporthelper.bestfit.curvefit
- Add ODRFit (wrapper for scipy.odr) to labreporthelper.bestfit.curvefit

0.2.1
-----
- Change kwargs for ODR, Data, RealData, Model to ODR_kwargs, Data_kwargs, ... in labreporthelper.bestfit.curvefit.ODRFit
- Add option to just add model instead of function in labreporthelper.bestfit.curvefit.ODRFit
