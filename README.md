# Auto-GTAP

Auto-GTAP combines all steps of running a GTAP-based research project into a single automated framework.

## Why use Auto-GTAP?

In principle, a GTAP simulation can be run with a single command. However, GTAP-based research projects usually contain more than just the model simulation. A project may also need to build a database, change aggregations, modify parameters, calculate shocks, or run multiple simulations, all the while shuffle around various files at each stage. While a single model simulation is already automated, these other task are not.

Auto-GTAP combines all these tasks into a single automated framework. By reducing the amount of manual orchestration required to run a GTAP project, Auto-GTAP will increase the speed and replicability of your analysis.

## Getting started

### Prerequisites

Mandatory
- Python 3.6 (other versions untested)
- Pyyaml 4.2b4 (other versions untested)
- GEMPACK 12.1 Limited Executable-Image Version (other versions untested)
    - You may have to reboot after installation.
    - [Download here](https://www.copsmodels.com/gpeidl.htm).
    - GEMPACK requires a license (licen.gem). You can use a GEMPACK license if you have one, but the download also comes with a free 6 month license.

Additional requirements for GTAP-E Validation advanced example
- GEMPACK 14.0 (other versions untested, [purchase information](https://www.copsmodels.com/gempack.htm))

Additional requirements for Productivity Increase advanced example
- GEMPACK 14.0 (other versions untested, [purchase information](https://www.copsmodels.com/gempack.htm))
- GTAP Data File v10_2014 ([purchase information](https://www.gtap.agecon.purdue.edu/databases/default.asp))
 
### Installation Instructions
 
 - Install [GEMPACK Limited Executable](https://www.copsmodels.com/gpeidl.htm) and reboot
 - Install [Python 3.6.3](https://www.python.org/downloads/release/python-363/)
 - Install Pyyaml 4.2b4
 **Where do I run this command? python console, cmd? in what directory?**
 ```bash
 pip install PyYAML==4.2b4
 ```
 - Clone the Repository
**Insert instructions here for how to do so in PyCharm**

### Running Auto-GTAP
- In PyCharm go to Run > Edit Configurations ...
- Click "+"
- Name your configuration "Main" and set the following settings:
    - Script path: ```main.py```
    - Working directory. Depends on example. For example: ```examples\productivity-increase-simple```
- Set Source root: ```src```
    - File > Settings > Project: "Project Name" > Project Structure
    - Click "src" and click "Sources"

### (Optional) For productivity increase advanced example

This example includes a step to aggregate GTAP data, and thus requires the disaggregated data file from GTAP. This data file is not freely available but must be [purchased from GTAP](https://www.gtap.agecon.purdue.edu/databases/default.asp). Thus we have not included it with Auto-GTAP: users must manually acquire it and place it into Auto-GTAP.

The specific data used in this example was the PR2_v10_2014_Sep2017 release of GTAPg2. It was located in 

````GTPAg2\GTAP10p2\GTAP\2014````

and should be placed in

````Auto-GTAP\examples\productivity_increase\InputFiles\GTPAg2\GTAP10p2\GTAP\2014````

## Example projects

- [Productivity Increase (Simple)](examples/productivity-increase-simple)
- [Productivity Increase (Advanced)](examples/productivity-increase-advanced)
- [GTAP-E Validation (Simple)](examples/gtap-e-validation-simple)
- [GTAP-E Validation (Advanced)](examples/gtap-e-validation-advanced)

## Documentation

- [Components of Auto-GTAP](docs/components-of-auto-gtap.md)
- [GTAP Prior to Auto-GTAP](docs/gtap-prior-to-auto-gtap.md)
