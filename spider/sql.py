# -*- encoding:utf-8 -*-
# Copyright (c) 2015 Shiye Inc.
# All rights reserved.
#
# Author: ldq <liangduanqi@shiyejinrong.com>
# Date: 2019/2/15 10:10


create_table_sql = """
        create table bgm_data_info(
id INT primary key auto_increment,
j_anime_name text,
c_anime_name text,
episode_number text,
broadcasting_start_date text,
layout text,
original text,
director text,
script text,
music text,
character_setting text,
total_painting text,
anime_make text,
art_design text,
official_website text,
alias text,
TV text,
broadcasting_end_date text,
copyright text,
make text,
xiangkan text,
kanguo text,
zaikan text,
gezhi text,
paoqi text,
total_score_number text,
score text,
ranking text,
score_1 text,
score_2 text,
score_3 text,
score_4 text,
score_5 text,
score_6 text,
score_7 text,
score_8 text,
score_9 text,
score_10 text
);
"""


insert_data_sql = '''
insert into bgm_data_info(
j_anime_name,
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
score_10
) VALUES (
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
%s,%s,%s,%s,%s,%s,%s
)
'''