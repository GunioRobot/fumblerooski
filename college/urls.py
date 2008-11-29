from django.conf.urls.defaults import *

urlpatterns = patterns('fumblerooski.college.views',
     url(r'^seasons/(?P<season>\d+)/week/(?P<week>\d+)/$', 'season_week'),
     url(r'^rankings/$', 'rankings_index'),
     url(r'^rankings/(?P<rankingtype>[-a-z]+)/(?P<season>\d+)/$', 'rankings_season'),
     url(r'^rankings/(?P<rankingtype>[-a-z]+)/(?P<season>\d+)/week/(?P<week>\d+)/$', 'rankings_season'),
     url(r'^conferences/$', 'conference_index'),
     url(r'^conferences/(?P<conf>[-a-z0-9]+)/(?P<season>\d+)/$', 'conference_detail'),
     url(r'^games/$', 'game_index'),
     url(r'^bowl-games/$', 'bowl_games'),
     url(r'^bowl-games/(?P<bowl>[-a-z]+)/$', 'bowl_game_detail'),
     url(r'^coaches/(?P<coach>[-a-z]+)/$', 'coach_detail'),
     url(r'^teams/$', 'team_index'),
     url(r'^teams/undefeated/(?P<season>\d+)/$', 'undefeated_teams'),
     url(r'^teams/(?P<team>[-a-z]+)/$', 'team_detail'),
     url(r'^teams/(?P<team>[-a-z]+)/bowl-games/$', 'team_bowl_games'),
     url(r'^teams/(?P<team>[-a-z]+)/offense/$', 'team_offense'),
     url(r'^teams/(?P<team>[-a-z]+)/offense/rushing/$', 'team_offense_rushing'),
     url(r'^teams/(?P<team>[-a-z]+)/defense/$', 'team_defense'),
     url(r'^teams/(?P<team>[-a-z]+)/penalties/$', 'team_penalties'),
     url(r'^teams/(?P<team>[-a-z]+)/first-downs/$', 'team_first_downs'),     
     url(r'^teams/(?P<team>[-a-z]+)/first-downs/(?P<category>rushing|passing|penalty)/$', 'team_first_downs_category'),
#     url(r'^teams/(?P<team>[-a-z]+)/positions/(?<pos>[a-z][a-z][a-z]?)/$', 'team_position_detail'),
     url(r'^teams/(?P<team>[-a-z]+)/(?P<season>\d+)/$', 'team_detail_season'),
     url(r'^teams/(?P<team>[-a-z]+)/(?P<season>\d+)/rankings/$', 'team_rankings_season'),
     url(r'^teams/(?P<team>[-a-z]+)/(?P<season>\d+)/classes/(?P<cl>[fr|so|jr|sr])/$', 'team_by_cls'),
     url(r'^teams/(?P<team>[-a-z]+)/opponents/$', 'team_opponents'),
     url(r'^teams/(?P<team>[-a-z]+)/(?P<season>\d+)/players/$', 'team_players'),
     url(r'^teams/(?P<team>[-a-z]+)/(?P<season>\d+)/players/(?P<player>[-a-z]+)/$', 'player_detail'),
     url(r'^teams/(?P<team1>[-a-z]+)/vs/(?P<team2>[-a-z]+)/$', 'team_vs'),
     url(r'^teams/(?P<team1>[-a-z]+)/vs/(?P<team2>[-a-z]+)/(?P<outcome>wins|losses|ties)/$', 'team_vs'),
     url(r'^teams/(?P<team1>[-a-z]+)/vs/(?P<team2>[-a-z]+)/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', 'game'),
     url(r'^teams/(?P<team1>[-a-z]+)/vs/(?P<team2>[-a-z]+)/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/drives/$', 'game_drive'),     
     url(r'^states/$', 'state_index'),
     url(r'^states/(?P<state>[a-z][a-z])/$', 'state_detail'),
)