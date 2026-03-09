-- ============================================================
-- hw01-starting-with-sql  |  02_seed.sql
-- Database: manga
-- 38 rows with intentional edge cases:
--   * NULL avg_rating (Berserk -- unrated)
--   * Single-volume completed series (Perfect Blue)
--   * Very long-running ongoing series (One Piece: 108 vols)
--   * Wide year range (1952 – 2019)
--   * Multiple genres: Shonen, Seinen, Shojo, Josei, Isekai,
--     Action, Horror, Thriller, Mecha, Slice of Life
--   * Authors with multiple titles (Takehiko Inoue, Rumiko Takahashi)
--   * avg_rating = 5.0 edge case (Perfect Blue)
--   * avg_rating in [3.0, 4.0] range (No Longer Human: 3.8)
-- ============================================================

INSERT INTO manga (title, author, genre, status, avg_rating, volumes, year_published)
VALUES
  ('Naruto',                  'Masashi Kishimoto',   'Shonen',        'Completed', 4.8, 72,  1999),
  ('One Piece',               'Eiichiro Oda',        'Shonen',        'Ongoing',   4.9, 108, 1997),
  ('Attack on Titan',         'Hajime Isayama',      'Seinen',        'Completed', 4.9, 34,  2009),
  ('My Hero Academia',        'Kohei Horikoshi',     'Shonen',        'Ongoing',   4.4, 38,  2014),
  ('Demon Slayer',            'Koyoharu Gotouge',    'Shonen',        'Completed', 4.7, 23,  2016),
  ('Death Note',              'Tsugumi Ohba',        'Thriller',      'Completed', 4.9, 12,  2003),
  ('Fullmetal Alchemist',     'Hiromu Arakawa',      'Action',        'Completed', 4.9, 27,  2001),
  ('Dragon Ball',             'Akira Toriyama',      'Shonen',        'Completed', 4.8, 42,  1984),
  ('Bleach',                  'Tite Kubo',           'Shonen',        'Completed', 4.3, 74,  2001),
  ('Hunter x Hunter',         'Yoshihiro Togashi',   'Shonen',        'Ongoing',   4.9, 37,  1998),
  ('Nana',                    'Ai Yazawa',           'Josei',         'Ongoing',   4.6, 21,  2000),
  ('Fruits Basket',           'Natsuki Takaya',      'Shojo',         'Completed', 4.7, 23,  1998),
  ('Vinland Saga',            'Makoto Yukimura',     'Seinen',        'Ongoing',   4.9, 27,  2005),
  ('Berserk',                 'Kentaro Miura',       'Seinen',        'Ongoing',   NULL, 41, 1989),
  ('Vagabond',                'Takehiko Inoue',      'Seinen',        'Ongoing',   4.8, 37,  1998),
  ('Slam Dunk',               'Takehiko Inoue',      'Shonen',        'Completed', 4.7, 31,  1990),
  ('Sailor Moon',             'Naoko Takeuchi',      'Shojo',         'Completed', 4.5, 18,  1991),
  ('Cardcaptor Sakura',       'CLAMP',               'Shojo',         'Completed', 4.6, 12,  1996),
  ('Soul Eater',              'Atsushi Ohkubo',      'Shonen',        'Completed', 4.3, 25,  2004),
  ('Black Clover',            'Yuki Tabata',         'Shonen',        'Ongoing',   4.1, 35,  2015),
  ('Overlord',                'Kugane Maruyama',     'Isekai',        'Ongoing',   4.5, 14,  2012),
  ('No Longer Human',         'Usamaru Furuya',      'Seinen',        'Completed', 3.8, 3,   2009),
  ('Yotsuba&!',               'Kiyohiko Azuma',      'Slice of Life', 'Ongoing',   4.9, 15,  2003),
  ('Mushishi',                'Yuki Urushibara',     'Seinen',        'Completed', 4.8, 10,  1999),
  ('Lone Wolf and Cub',       'Kazuo Koike',         'Seinen',        'Completed', 4.6, 28,  1970),
  ('Astro Boy',               'Osamu Tezuka',        'Shonen',        'Completed', 4.2, 23,  1952),
  ('Gintama',                 'Hideaki Sorachi',     'Shonen',        'Completed', 4.8, 77,  2003),
  ('Spy x Family',            'Tatsuya Endo',        'Action',        'Ongoing',   4.8, 12,  2019),
  ('Chainsaw Man',            'Tatsuki Fujimoto',    'Action',        'Ongoing',   4.7, 11,  2018),
  ('Jujutsu Kaisen',          'Gege Akutami',        'Shonen',        'Ongoing',   4.6, 21,  2018),
  ('The Promised Neverland',  'Kaiu Shirai',         'Shonen',        'Completed', 4.5, 20,  2016),
  ('Tokyo Ghoul',             'Sui Ishida',          'Horror',        'Completed', 4.3, 14,  2011),
  ('Claymore',                'Norihiro Yagi',       'Action',        'Completed', 4.4, 27,  2001),
  ('Neon Genesis Evangelion', 'Yoshiyuki Sadamoto',  'Mecha',         'Completed', 4.5, 14,  1994),
  ('Perfect Blue',            'Yoshikazu Takeuchi',  'Horror',        'Completed', 5.0, 1,   1997),
  ('Doraemon',                'Fujiko F. Fujio',     'Slice of Life', 'Completed', 4.5, 45,  1969),
  ('Ranma 1/2',               'Rumiko Takahashi',    'Shonen',        'Completed', 4.4, 38,  1987),
  ('Inuyasha',                'Rumiko Takahashi',    'Action',        'Completed', 4.3, 56,  1996);
