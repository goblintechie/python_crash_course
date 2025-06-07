# 在8-7中编写一个while循环，让用户输入专辑的歌手和名称
# 获得这些信息后，用他们调用函数make_album()将创建的字典打印出来
# while循环务必提供退出途径

def make_album(singer_name,album_name):
    """函数创建一个包含歌手名和专辑名的字典"""
    album = {'singer name':singer_name,'album name':album_name}
    return album

while True:
    print("请输入歌手名称和专辑名称，退出请输入'q'。")
    s_name = input("请输入歌手名称：")
    a_name = input("请输入专辑名称：")
    
    album = make_album(s_name,a_name)
    print(album)

    if s_name or a_name == "q":
        break
