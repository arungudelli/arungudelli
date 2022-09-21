+++
title="Save Datatable Information Into Database"
summary="This Post will explain How we can save Datatable or Data Set information to Data base.I tried to explain this in detail,but a primary knowledge on C#,Xml,Sql is"
keywords=["asp .net"
]
type='post'
date='2019-08-17T18:09:22+0000'
lastmod='2019-08-17T18:09:22+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
caption='Save Datatable Information Into Database'
focal_point=''
preview_only=false
+++


This Post will explain How we can save Datatable or Data Set information to Data base.
I tried to explain this in detail,but a primary knowledge on C#,Xml,Sql is required.

Steps as follows.

1. Save Data to a datatable
2. insert Datatable into a dataset
3. Convert the dataset into XmlString
4. Send this Xml string to a StoredProcedure Which will parse the Xml and Save the data into DataBase.

## Creating a Table:

```
Create table Student{
Name varachar2(50),
Address varachar2(50),
Phone varachar2(50),
}
```

## Data Table Creation And DataSet:

```
public static DataSet GetDataSetInfo()
{
    DataSet ds = new DataSet();
    DataTable dt = new DataTable(“Sample”);
    
    dt.Columns.Add(“Name”, Type.GetType(“System.String”));
    dt.Columns.Add(“Address”, Type.GetType(“System.String”));
    dt.Columns.Add(“Phone”, Type.GetType(“System.String”));
    
    DataRow dr = dt.NewRow();
    dr[“Name”] = “Srinivas”;
    dr[“Address”] = “Banglore”;
    dr[“Phone”] = “+91-9999912345”;
    dt.Rows.Add(dr);
    
    dr = dt.NewRow();
    dr[“Name”] = “Ravi”;
    dr[“Address”] = “Mumbai”;
    dr[“Phone    “] = “+91-9888894444”;
    dt.Rows.Add(dr);
    
    ds.Tables.Add(dt);
    return ds    ;
}
```

## Convert Dataset Into Xml String:

```
public static string DataSetToXMLString(DataTable dt)
{
    DataSet ds = new DataSet();
    string XMLformat;
    try
    {
        StringBuilder sb = new StringBuilder();
        StringWriter sw = new StringWriter(sb);
        ds.Merge(dt, true, MissingSchemaAction.AddWithKey);
        ds.Tables[0].TableName = “SampleTable”;
        foreach (DataColumn column in ds.Tables[0].Columns)
        {
            column.ColumnMapping = MappingType.Attribute;
        }
        ds.WriteXml(sw, XmlWriteMode.WriteSchema);
        XMLformat = sb.ToString();
        return XMLformat;
    }
    catch (Exception Exception)
    {
        throw Exception;
    }
}
```

## The Main Method:

```
static void Main(string[] args)
{
    DataSet ds = GetDataSet();
    String xmlData = DataSetToXMLString(ds.Tables[0]);
    SqlConnection conn = new SqlConnection
    (“Data Source=.;Initial Catalog=DBName;Integrated Security=SSPI;”);
    SqlCommand command = new SqlCommand
    (“InsertData ‘” + xmlData + “‘”, conn);
     conn.Open();
     command.ExecuteNonQuery();
     conn.Close();
}
```

## Stored Procedure:

```
This is very Important as it parses the xml String And Save into Database.

```
CREATE PROCEDURE InsertData (@xmlString VARCHAR(MAX))
AS
BEGIN
       DECLARE @xmlHandle INT 
       DECLARE @dummyTable TABLE 
     ( 
        [Name]   VARCHAR(50), 
        [Address]  VARCHAR(50), 
        [Phone]   VARCHAR(50)
     ) 
 
        EXEC sp_xml_preparedocument @xmlHandle output, @xmlString  
 INSERT INTO @dummyTable 
  SELECT  [Name] ,[Address],[Phone] 
  FROM  OPENXML (@xmlHandle, ‘/NewDataSet/SampleDataTable’,1) 
     WITH ( [Name]  varchar(50)  ‘@Name’, 
           [Address]  varchar(50)  ‘@Address’, 
           [Phone]  varchar(50)  ‘@Phone’
         )
 INSERT INTO SampleData ([Name],[Address], [Phone]) 
  (SELECT [Name] ,[Address],[Phone]
  FROM @dummyTable)
 EXEC sp_xml_removedocument @xmlHandle
END
```

If you have any doubts feel free to contact me..









