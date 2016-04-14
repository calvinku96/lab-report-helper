labreporthelper
===============

Module in python to help in automating lab reports

Documentation: <http://labreporthelper.readthedocs.org/en/latest/>

Installations
-------------
Clone and run
```
pip install labreporthelper
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

0.2.2
-----
- Add wrapper functions for bestfit in labreporthelper.bestfit.bestfit

0.2.1
-----
- Change kwargs for ODR, Data, RealData, Model to ODR_kwargs, Data_kwargs, ... in labreporthelper.bestfit.curvefit.ODRFit
- Add option to just add model instead of function in labreporthelper.bestfit.curvefit.ODRFit

0.2
---
- Add CurveFit (wrapper for scipy.optimize.curvefit) to labreporthelper.bestfit.curvefit
- Add ODRFit (wrapper for scipy.odr) to labreporthelper.bestfit.curvefit
