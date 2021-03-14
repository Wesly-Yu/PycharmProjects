# coding:utf-8
'''
/**
 * @author Wesley -Yu
 * @date 2020/12/17
 */
'''

from pathlib import Path
import configparser

paths = ["resource","config.ini"]
osp=Path.cwd().parent.joinpath(*paths)
cf = configparser.ConfigParser()
cf.read(osp)
browser = cf.get("Options","browser")
head=cf.get('Options', 'headless')
