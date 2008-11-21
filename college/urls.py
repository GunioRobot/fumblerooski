from django.conf.urls.defaults import *


urlpatterns = patterns('fumblerooski.college.views',
     (r'^college/seasons/(?P<season>\d+)/week/(?P<week>\d+)/$', 'season_week'),
     (r'^college/conferences/$', 'conference_index'),
     (r'^college/conferences/(?P<conf>[-a-z0-9]+)/(?P<season>\d+)/$', 'conference_detail'),
     (r'^college/games/$', 'game_index'),
     (r'^college/coaches/(?P<coach>[-a-z]+)/$', 'coach_detail'),
     (r'^college/teams/$', 'team_index'),
     (r'^college/teams/undefeated/(?P<season>\d+)/$', 'undefeated_teams'),
     (r'^college/teams/(?P<team>[-a-z]+)/$', 'team_detail'),
     (r'^college/teams/(?P<team>[-a-z]+)/offense/$', 'team_offense'),
     (r'^college/teams/(?P<team>[-a-z]+)/offense/rushing/$', 'team_offense_rushing'),
     (r'^college/teams/(?P<team>[-a-z]+)/defense/$', 'team_defense'),
     (r'^college/teams/(?P<team>[-a-z]+)/penalties/$', 'team_penalties'),
     (r'^college/teams/(?P<team>[-a-z]+)/first-downs/$', 'team_first_downs'),     
     (r'^college/teams/(?P<team>[-a-z]+)/first-downs/(?P<category>rushing|passing|penalty)/$', 'team_first_downs_category'),
     (r'^college/teams/(?P<team>[-a-z]+)/positions/(?<pos>[a-z][a-z][a-z]?)/$', 'team_position_detail'),
     (r'^college/teams/(?P<team>[-a-z]+)/(?P<season>\d+)/$', 'team_detail_season'),
     (r'^college/teams/(?P<team>[-a-z]+)/(?P<season>\d+)/rankings/$', 'team_rankings_season'),
     (r'^college/teams/(?P<team>[-a-z]+)/(?P<season>\d+)/classes/(?P<cl>[fr|so|jr|sr])/$', 'team_by_cls'),
#     (r'^college/teams/(?P<team>[-a-z]+)/(?P<season>\d+)/positions/(?<pos>[a-z][a-z][a-z]?)/$', team_positions),
     (r'^college/teams/(?P<team>[-a-z]+)/opponents/$', 'team_opponents'),
     (r'^college/teams/(?P<team>[-a-z]+)/(?P<season>\d+)/players/$', 'team_players'),
     (r'^college/teams/(?P<team>[-a-z]+)/(?P<season>\d+)/players/(?P<player>[-a-z]+)/$', 'player_detail'),
     (r'^college/teams/(?P<team1>[-a-z]+)/vs/(?P<team2>[-a-z]+)/$', 'team_vs'),
     (r'^college/teams/(?P<team1>[-a-z]+)/vs/(?P<team2>[-a-z]+)/(?P<outcome>wins|losses|ties)/$', 'team_vs'),
     (r'^college/teams/(?P<team1>[-a-z]+)/vs/(?P<team2>[-a-z]+)/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', 'game'),
     (r'^college/teams/(?P<team1>[-a-z]+)/vs/(?P<team2>[-a-z]+)/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/drives/$', 'game_drive'),     
     (r'^states/$', 'state_index'),
     (r'^states/(?P<state>[a-z][a-z])/$', 'state_detail'),
)