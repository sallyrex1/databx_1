# Databricks notebook source
# MAGIC %md
# MAGIC ##### Running NoteBooks Directly

# COMMAND ----------

# MAGIC %run "/Workspace/Users/rexford.osei-aboagye@cognizant.com/databx_1/data-engineer-learning-path-v1-0-2-notebooks (1)/Includes/Classroom-Setup-02.1"

# COMMAND ----------

print('DA.paths.kafka_events') # look for the content of the define path

src = dbutils.fs.ls(DA.paths.kafka_events)
display(src) # see what it entails

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM JSON.`${DA.paths.kafka_events}/010.json`  --sample data of what is in each folder
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM JSON.`${DA.paths.kafka_events}` -- query the entire folder
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Create Temp views or views

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE VIEW 02_TempViews
# MAGIC AS
# MAGIC SELECT * FROM JSON.`${DA.paths.kafka_events}` 
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM 02_TempViews LIMIT 3

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM TEXT.`${DA.paths.kafka_events}` LIMIT 5

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM binaryFile.`${DA.paths.kafka_events}` LIMIT 5

# COMMAND ----------

DA.cleanup()

# COMMAND ----------


