import sys
import os
import yaml

class FilesClass:
    def __init__(self):
        self.path = sys.path[1]#脚本运行路径
        print("Current Path:"+self.path)
        self.path = self.path + "/ESP_TOOL"
        try:
            os.mkdir(self.path)
        except:
            pass
        # try:#如果有Config文件就打开阅读，如果没有创建
        self.ProjectData = {
            "PATH": self.path,
            "Port": "COM0",
        }
        with open(self.path+'/Config.yml','w+',encoding='utf-8') as f:#文件
            result = yaml.load(f.read(),Loader=yaml.FullLoader)#读取
            if result == None:#如果文件是空的，进入条件，写入默认值
                print("Write")
                yaml.dump(data=self.ProjectData,stream=f,allow_unicode=True)
            print(result)#调试打印
            f.close()#关闭文档
    def ChangePort(self,Port):#改变文档Port
        self.ProjectData['Port'] = Port
        with open(self.path+'Config.yml','w+',encoding='utf-8')as f:
            yaml.dump(data=self.ProjectData,stream=f,allow_unicode=True)#写入
            f.close()
