from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (StageToRedshiftOperator, LoadFactOperator,
                                LoadDimensionOperator, DataQualityOperator)
from helpers import SqlQueries

# AWS_KEY = os.environ.get('AWS_KEY')
# AWS_SECRET = os.environ.get('AWS_SECRET')

default_args = {
    'owner': 'udacity',
    'start_date': datetime(2019,1,1),
    #'retries': 3,
    #'retry_delay': timedelta(minutes=5),
    'email_on_failure': False,
    'depends_on_past': False,
    'email_on_retry': False,
}

dag = DAG('udac_example_dag',
          default_args=default_args,
          description='Load and transform data in Redshift with Airflow',
          #schedule_interval='0 * * * *',
          catchup=False
        )

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

#stage_events_to_redshift = StageToRedshiftOperator(
#    task_id='Stage_events',
#    dag=dag,
#    table="staging_events",
#    redshift_conn_id="redshift",
#    aws_credentials_id="aws_credentials",
#    s3_bucket="s3://udacity-dend/log_data"
#    #s3_key="divvy/partitioned/{execution_date.year}/{execution_date.month}/divvy_trips.csv"
#)

#stage_songs_to_redshift = StageToRedshiftOperator(
#    task_id='Stage_songs',
#    dag=dag,
#    table="staging_songs",
#    redshift_conn_id="redshift",
#    aws_credentials_id="aws_credentials",
#    s3_bucket="s3://udacity-dend/song_data",
#)

#load_songplays_table = LoadFactOperator(
#    task_id='Load_songplays_fact_table',
#    dag=dag
#)

#load_user_dimension_table = LoadDimensionOperator(
#    task_id='Load_user_dim_table',
#    dag=dag
#)

#load_song_dimension_table = LoadDimensionOperator(
#    task_id='Load_song_dim_table',
#    dag=dag
#)

#load_artist_dimension_table = LoadDimensionOperator(
#    task_id='Load_artist_dim_table',
#    dag=dag
#)

#load_time_dimension_table = LoadDimensionOperator(
#    task_id='Load_time_dim_table',
#    dag=dag
#)

#run_quality_checks = DataQualityOperator(
#    task_id='Run_data_quality_checks',
#    dag=dag
#)

#end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)

#start_operator >> stage_events_to_redshift
#start_operator >> stage_songs_to_redshift
#stage_events_to_redshift >> load_songplays_table
#stage_songs_to_redshift >> load_songplays_table
#load_songplays_table >> load_user_dimension_table
#load_songplays_table >> load_song_dimension_table
#load_songplays_table >> load_artist_dimension_table
#load_songplays_table >> load_time_dimension_table
#load_user_dimension_table >> run_quality_checks
#load_song_dimension_table >> run_quality_checks
#load_artist_dimension_table >> run_quality_checks
#load_time_dimension_table >> run_quality_checks
#run_quality_checks >> end_operator
