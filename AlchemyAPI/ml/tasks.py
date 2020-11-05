from pipeline import Pipeline

pipeline = Pipeline()
pipeline.create_pipeline()
pipeline.ingest_data()
pipeline.prepare_data()
pipeline.train()
pipeline.evaluate()
pipeline.deploy()