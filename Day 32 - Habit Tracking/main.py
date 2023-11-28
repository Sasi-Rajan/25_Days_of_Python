import requests as req
from datetime import datetime
USERNAME="sasirajan"
TOKEN="endpoint"
pixela_end_point_api="https://pixe.la/v1/users"
pixela_end_point_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
#TODO Create user
# response=req.post(url=pixela_end_point_api,json=pixela_end_point_params)
graph_creation_endpoint=f"{pixela_end_point_api}/{USERNAME}/graphs"
graph_config={
    "id":"graph1",
    "name":"Learning Duration",
    "unit":"Min",
    "type":"int",
    "color":"momiji",
}
headers={
    "X-USER-TOKEN":TOKEN
}
# TODO Graph creation
# response=req.post(url=graph_creation_endpoint,json=graph_config,headers=headers)
# print(response.text)

# #TODO Posting Value to my graph
today=datetime.now()
pixel_creation_endpoint=f"{pixela_end_point_api}/{USERNAME}/graphs/graph1"
pixel_data={
    "date":today.strftime(r"%Y%m%d"),
    "quantity":input("How many minutes did you learned a skill today? "),
}
response=req.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)

# TODO Put(update) the data on the graph
# put_data_config={
#     "quantity":"200"
# }
# put_data_on_graph_api=f"{pixela_end_point_api}/{USERNAME}/graphs/graph1/{today.strftime(r"%Y%m%d")}"
# response=req.put(url=put_data_on_graph_api,headers=headers,json=put_data_config)

# #TODO Deleting pixels in the console
# delete_endpoint_api=f"{pixela_end_point_api}/{USERNAME}/graphs/graph1/{today.strftime(r"%Y%m%d")}"
# response=req.delete(url=delete_endpoint_api,headers=headers)
# print(response.text)