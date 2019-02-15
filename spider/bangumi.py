# -*- encoding:utf-8 -*-
# Copyright (c) 2015 Shiye Inc.
# All rights reserved.
#
# Author: ldq <liangduanqi@shiyejinrong.com>
# Date: 2019/2/13 16:49

import requests
from scrapy import Selector

from db import POOL
from sql import create_table_sql, insert_data_sql

conn = POOL.connection()
cursor = conn.cursor()


def get_text(url):
    res_text = requests.get(url).text
    url_list = Selector(text=res_text).xpath(
        "//div[@class='section']//li/a/@href").extract()
    for url in url_list:
        url = 'http://bangumi.tv/' + url
        res = requests.get(url)
        res.encoding = 'utf-8'
        detail_text = res.text

        j_anime_name = Selector(text=detail_text).xpath(
            "//h1/a/text()").extract_first()
        c_anime_name = Selector(text=detail_text).xpath(
            "//h1/a/@title").extract_first()
        # 话数
        episode_number = Selector(text=detail_text).xpath(
            "//span[contains(text(),'话数:')]/../text()").extract_first()
        # 放送开始:
        broadcasting_start_date = Selector(text=detail_text).xpath(
            "//span[contains(text(),'放送开始:')]/../text()").extract_first()
        # 原作:
        original = Selector(text=detail_text).xpath(
            "//span[contains(text(),'原作:')]/../a/text()").extract_first()
        # 导演:
        director = Selector(text=detail_text).xpath(
            "//span[contains(text(),'导演:')]/../a/text()").extract_first()
        # 脚本
        script = Selector(text=detail_text).xpath(
            "//span[contains(text(),'脚本:')]/../a/text()").extract_first()
        # 分镜
        # 演出
        # 音乐
        music = Selector(text=detail_text).xpath(
            "//span[contains(text(),'音乐:')]/../a/text()").extract_first()
        # 人物设定
        character_setting = Selector(text=detail_text).xpath(
            "//span[contains(text(),'人物设定:')]/../a/text()").extract_first()
        # 系列构成
        # 美术监督
        # 总作画监督
        total_painting = Selector(text=detail_text).xpath(
            "//span[contains(text(),'总作画监督:')]/../a/text()").extract_first()
        # 作画监督
        # 机械监督
        # 摄影监督
        # 原画
        # 动画检查
        # 背景美术
        # 设定
        # 系列监督
        # 音响监督
        # 制片人
        # 制作
        # 动画制作
        anime_make = Selector(text=detail_text).xpath(
            "//span[contains(text(),'动画制作:')]/../a/text()").extract_first()
        # 美术设计
        art_design = Selector(text=detail_text).xpath(
            "//span[contains(text(),'美术设计:')]/../a/text()").extract_first()
        # OP・ED分镜
        # 官方网站
        official_website = Selector(text=detail_text).xpath(
            "//span[contains(text(),'官方网站:')]/../text()").extract_first()
        # 播放电视台
        TV = Selector(text=detail_text).xpath(
            "//span[contains(text(),'播放电视台:')]/../text()").extract_first()
        # 总导演
        # 副导演
        # 别名
        alias = Selector(text=detail_text).xpath(
            "//span[contains(text(),'别名:')]/../text()").extract_first()
        # 播放结束
        broadcasting_end_date = Selector(text=detail_text).xpath(
            "//span[contains(text(),'播放结束:')]/../text()").extract_first()
        # 企画
        layout = Selector(text=detail_text).xpath(
            "//span[contains(text(),'企画:')]/../text()").extract_first()
        # Copyright
        copyright = Selector(text=detail_text).xpath(
            "//span[contains(text(),'Copyright:')]/../text()").extract_first()
        # 製作
        make = Selector(text=detail_text).xpath(
            "//span[contains(text(),'Copyright:')]/../text()").extract_first()

        # 想看
        # 看过
        # 在看
        # 搁置
        # 抛弃
        look_list = Selector(text=detail_text).xpath(
            "//div[@id='subjectPanelCollect']//span[@class='tip_i']/a/text()"
        ).extract()
        xiangkan, kanguo, zaikan, gezhi, paoqi = [look.split("人")[0] for look in
                                                  look_list]
        print(xiangkan)

        # 评分总人数
        total_score_number = Selector(text=detail_text).xpath(
            "//div[@id='ChartWarpper']//small//span/text()"
        ).extract_first()
        # 分数
        score = Selector(text=detail_text).xpath(
            "//div[@class='global_score']/span[@class='number']/text()"
        ).extract_first()

        ranking = Selector(text=detail_text).xpath(
            "//div[@class='global_score']/div/small[@class='alarm']/text()"
        ).extract_first()

        score_list = Selector(text=detail_text).xpath(
            "//ul[@class='horizontalChart']/li/a/@title").extract()
        (score_10, score_9, score_8, score_7, score_6, score_5,
         score_4, score_3, score_2, score_1) = [score.split("人")[0] for score in
                                                score_list]


        execute_sql(insert_data_sql, (j_anime_name,
                                      c_anime_name,
                                      episode_number,
                                      broadcasting_start_date,
                                      layout,
                                      original,
                                      director,
                                      script,
                                      music,
                                      character_setting,
                                      total_painting,
                                      anime_make,
                                      art_design,
                                      official_website,
                                      alias,
                                      TV,
                                      broadcasting_end_date,
                                      copyright,
                                      make,
                                      xiangkan,
                                      kanguo,
                                      zaikan,
                                      gezhi,
                                      paoqi,
                                      total_score_number,
                                      score,
                                      ranking,
                                      score_1,
                                      score_2,
                                      score_3,
                                      score_4,
                                      score_5,
                                      score_6,
                                      score_7,
                                      score_8,
                                      score_9,
                                      score_10))

        print(url)
        print(score_10)


def execute_sql(sql, args):

    # print(sql)
    # print(args)
    if not args:
        res = cursor.execute(sql)
        conn.commit()
    else:
        res = cursor.execute(sql, args)
        conn.commit()
        # cursor.close()
        # conn.close()


if __name__ == '__main__':
    # execute_sql(create_table_sql)
    for i in range(1, 614):
        url = 'http://bangumi.tv/anime/browser?sort=rank&page=%s' % i
        get_text(url)
        # t = Thread(target=get_text,args=(url,))
        # t.start()
