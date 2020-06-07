<img src="https://www.mlflow.org/docs/latest/_static/MLflow-logo-final-black.png" width="200">

#### MLflow Lab Part 2: Projects and Models
         
This second lab is aimed to explain how to containerize/package models and projects using MLflow. 
All of that in the most simple and right to the point way!

&nbsp;

**MLflow Projects**

An MLflow Project is a format for packaging data science code in a reusable and reproducible way,
 based primarily on conventions. In addition, the Projects component includes an API and command-line
  tools for running projects, making it possible to chain together projects into workflows.
  
###### What's does a MLflow Project Look Like?

[MLflow Project Example](https://github.com/Isaac4real/MLflow_Project.git)

<img src="https://raw.githubusercontent.com/Isaac4real/MLflow_Experiment/master/Part2-%20MLflow%20Projects%26Models/Images/MLproject_structure.png" height="200">

&nbsp;

**MLflow Models**

An MLflow Model is a standard format for packaging machine learning models that can be used in
 a variety of downstream tools—for example, real-time serving through a REST API or batch 
 inference on Apache Spark. The format defines a convention that lets you save a model in
  different “flavors” that can be understood by different downstream tools.

###### What's does a MLflow Model Look Like?

<img src="https://raw.githubusercontent.com/Isaac4real/MLflow_Experiment/master/Part2-%20MLflow%20Projects%26Models/Images/ModelFolderStructure.png" height="200">

&nbsp;

&nbsp;
## Content
1. Introduction MLflow Projects module: API (command line and programmatically)
2. Configure Databricks CLI to be able to run MLproject from GitHub
3. Load and run the project form GitHub using `MLflow Fluent API` and `MLflow Project API`
4. Explore MLflow UI: check for conda.yaml, MLproject file and metrics
5. Replicate everything in your machine (locally)

 Series  Part 2 of 4
-----------
Other parts:
- [Part 1](https://github.com/Isaac4real/MLflow_Experiment/tree/master/Part1-%20MLflow%20Tracking)
- [Part 3](https://github.com/Isaac4real/MLflow_Experiment/tree/master/Part3-%20MLflow%20Registry)
- [Part 4](https://github.com/Isaac4real/MLflow_Experiment/tree/master/Part4-%20MLflow%20Registry_locally)