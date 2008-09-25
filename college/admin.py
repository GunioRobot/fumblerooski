from django.contrib import admin
from fumblerooski.college.models import Coach, College, CollegeCoach, Position, State, Game, CoachingJob, RankingType, Ranking, Week

class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    ordering = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class CoachAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CoachingJobAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CollegeCoachAdmin(admin.ModelAdmin):
    list_display = ('coach', 'college', 'job', 'start_date', 'end_date')

class GameAdmin(admin.ModelAdmin):
    list_display = ('team1', 'team2', 'date', 't1_result', 'team1_score', 'team2_score')
    ordering = ('-date',)
    list_filter = ('season','week')

class PlayerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class RankingTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class RankingAdmin(admin.ModelAdmin):
    list_filter = ('year', 'ranking_type')

class WeekAdmin(admin.ModelAdmin):
    list_filter = ('year',)

admin.site.register(College, CollegeAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(CoachingJob, CoachingJobAdmin)
admin.site.register(CollegeCoach, CollegeCoachAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(RankingType, RankingTypeAdmin)
admin.site.register(Ranking, RankingAdmin)
admin.site.register(Week, WeekAdmin)