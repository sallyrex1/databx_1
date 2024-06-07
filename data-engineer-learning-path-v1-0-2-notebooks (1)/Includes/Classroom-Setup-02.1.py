# Databricks notebook source
# MAGIC %md
# MAGIC ##### This have been amended with restarting the Python libray and also downgrading the cluster from 14.3 to 11.3

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %run ./_common

# COMMAND ----------

lesson_config = LessonConfig(name = None,
                             create_schema = True,
                             create_catalog = False,
                             requires_uc = False,
                             installing_datasets = True,
                             enable_streaming_support = False)

DA = DBAcademyHelper(course_config=course_config,
                     lesson_config=lesson_config)
DA.reset_lesson()
DA.init()

DA.paths.kafka_events = f"{DA.paths.datasets}/ecommerce/raw/events-kafka"

DA.conclude_setup()                      # Conclude setup by advertising environmental changes

# COMMAND ----------


