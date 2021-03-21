# coding:utf-8
'''
/**
 * @author Wesley -Yu
 * @date 2020/12/17
 */
'''

from pathlib import Path
import configparser

paths = ["Base","helium_script.py"]
osp=str(Path.cwd().parent.joinpath(*paths))
script = "python -m black "+osp
print(script)

# cf = configparser.ConfigParser()
# cf.read(osp)
# browser = cf.get("Options","browser")
# head=cf.get('Options', 'headless')
