import trimesh

tm = trimesh.load('/medias/db/ImagingSecurity_misc/Sahar/facescape/toolkit/point_cloud/2_1_neutral_pointCloud.ply')

print(tm.colors.shape)

print(tm.vertices.shape)