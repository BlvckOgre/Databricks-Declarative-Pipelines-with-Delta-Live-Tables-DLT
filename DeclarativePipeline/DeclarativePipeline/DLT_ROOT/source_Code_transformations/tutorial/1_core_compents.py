# # create streaming table
# import dlt

# @dlt.table(
#     name = "streaming_table1"
# )
# def streaming_table1():
#   df = spark.readStream.table("tuesday.source._orders")
#   return df

# #create a materialized view for batch data

# @dlt.table(
#     name = "materialized_view1"
# )
# def materialized_view1():
#   df = spark.read.table("tuesday.source._orders")
#   return df

# #create batch view
# @dlt.view(
#     name = "batch_view1"
# )
# def batch_view1():
#   df = spark.read.table("tuesday.source._orders")
#   return df

# #create streaming view 
# @dlt.view(
#     name = "streaming_view1"
# )
# def streaming_view1():
#   df = spark.readStream.table("tuesday.source._orders")
#   return df