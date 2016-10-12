LOAD CSV WITH HEADERS FROM "file:///C:/create_video.csv" AS line 

CREATE (video:Video { id: line.id, title: line.newtitle, description: line.newdesc})
;