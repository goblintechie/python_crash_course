# 编写一个make_album()函数，创建描述音乐专辑的字典
# 函数应该接受歌手的名字和专辑名，返回一个包含这两项信息的字典

def make_album(singer_name,album_name):
    """函数创建一个包含歌手名和专辑名的字典"""
    album = {'singer name':singer_name,'album name':album_name}
    return album

album1 = make_album('周杰伦','范特西')
print(album1)
