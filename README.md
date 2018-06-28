# Auto-GTAP Read Me

Auto-GTAP project is a project to create a modern cross-platform project format for CGE research.

## Overview

In principle, a GTAP simulation can be run with a single command. However, the reality is that the
process tends to be much more complicated. A typical GTAP-based research project will need to build
balance a database, calculate shocks, and shuffle around various files at each stage, in addition
to running the simulation itself, all before finally exporting simulation results.

While the simulation is an automated process, these ambient task require require user interaction.
Auto-GTAP aims to provide a unified framework to lift these ambient tasks into the build toolchain.
The goal is to increase the speed and replicability of GTAP-based analyses, by reducing the amount
of manual orchestration required historically.

## Why Auto-GTAP?

### Andre's version

The Global Trade Analysis Project (GTAP) model is frequently used to estimate the effect of government policies on international trade. However, the biggest advantage of the GTAP model is not the original model itself, but the ecosystem around it. The original version introduced in 1995 has been updated to version 7 in Corong et al. (2017) and contributors have developed other versions of it focusing on topics such as energy (GTAP-E), biofuels (GTAP-BIO), and land use (GTAP-AEZ). Perhaps the greatest advantage of the GTAP model is data availability. GTAP (the orginization behidn the GTAP model) also provides detailed and regularly updated databases of the world economy. As a result of these tools and data, many non-GTAP models are built using the [GTAP database](https://www.gtap.agecon.purdue.edu/about/data_models.asp).

As a result of the popularity of the GTAP model and database, developers have created a number of software tools for dealing with the anciliary issues that crop up in these research projects, especially with databases. There are tools automating the process of data aggregation (GTPAg2), disaggregation (SplitCom), revision (GTAP-Adjust and AlterTax). The existence of these tools makes it easy for developers to customize the model for their specific project, as they do not have to reinvent the wheel.

However, some parts of a GTAP-based research have not been automated. In particular, there is no overarching framework controlling both the model and all these tools: the process of running the tools, specifiying their settings, and moving the output to the input of other tools must all be done manually.

Until now. Auto-GTAP provides a unified framework for running all parts of a GTAP-based research project.

### Austin's version

The Global Trade Analysis Project (GTAP) model was developed in [19XX]() to estimate the effect
of government policies on international trade.

The popularity of the GTAP modeling framework is due in large part to the ecosystem of tools and 
model extensions developed and contributed by researchers over years.

Alongside the canonical model, contributors have developed numerous extensions to focus on a variety
of topics such as [energy](), [biofuels](), and [electricity](). 

Developers have also created a number of other software tools for dealing with the anciliary issues 
that crop up in these research projects, especially with databases. There are tools automating the 
process of data [aggregation](https://www.gtap.agecon.purdue.edu/products/packages.asp), 
[disaggregation](https://www.gtap.agecon.purdue.edu/resources/splitcom.asp), 
[other](https://www.copsmodels.com/archivep.htm) types of 
[revisions](https://www.copsmodels.com/webhelp/rungtap/index.html?hc_altertax.htm). The existence 
of these tools makes it possible for developers to tailor the model for their specific project.

However, some parts of a GTAP-based research have not been automated. In particular, there is no 
overarching framework controlling both the model and all these tools: the process of running the 
tools, specifying their settings, and moving the output to the input of other tools must all be 
done manually.

Auto-GTAP provides a framework to define a proper toolchain in GTAP-based research projects.

## Getting started

### Prerequisites

TODO: describe the environment
 
 
### Clone the repository 
 
 ```bash
cd your_project_directory

git clone https://github.com/andre-barbe/Auto-GTAP.git
```

### Create a Python virtual environment
 
```bash
python -m venv venv 
```

### Initialize the workspace

```bash
./setup.ps1
```

## Example projects

- [Hello World!](examples/hello_world_example)
- [Free Trade Agreement](examples/free_trade_agreement_example)

## Documentation

- [Components of Auto-GTAP](docs/components-of-auto-gtap.md)

## References
- [Corong et al. 2017](https://jgea.org/resources/jgea/ojs/index.php/jgea/article/view/47)
