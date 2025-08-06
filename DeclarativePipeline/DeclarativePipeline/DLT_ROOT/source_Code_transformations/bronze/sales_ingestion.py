import dlt

# sales expectations

sales_rules = {
    "rule" : "sales_id IS NOT NULL"
}

#Empty streaming table
dlt.create_streaming_table(
    name = "sales_stg",
    expect_all_or_drop = sales_rules
)

#create east_sales flow
@dlt.append_flow(target="sales_stg")
def east_sales():

    df = spark.readStream.table("tuesday.source.sales_east")
    return df

@dlt.append_flow(target="sales_stg")
def west_sales():

    df = spark.readStream.table("tuesday.source.sales_west")
    return df