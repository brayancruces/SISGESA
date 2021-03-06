#encoding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',


	#############################################MEDIA
	url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
	################################################

	url(r'^alumno/registrar$' , 'principal.views.registrar_alumnos'),
	url(r'^padre/registrar$' , 'principal.views.registrar_padres'),
	url(r'^padre/ver_hijos$' , 'principal.views.ver_hijos'),
	url(r'^profesores/$','principal.views.ver_lista_profesores',name='lista_profesores'),

	url(r'^padres/$' , 'principal.views.ver_lista_padres' , name='lista_padres'),
	

	url(r'^padre/ver_comunicados$' , 'principal.views.padre_ve_comunicados'),
	url(r'^colegio/ver_comunicados$' , 'principal.views.colegio_ve_comunicados'),

	url(r'^evento/registrar$' , 'principal.views.registrar_evento', name = 'registrar_evento'),
	url(r'^eventos/$' , 'principal.views.ver_eventos_alumno', name = 'ver_eventos_alumno'),

	
	url(r'^padre/(?P<username>.*)/lista_profesores$','principal.views.ver_lista_profesores'),

	url(r'^padres/$','principal.lista_padres.ver_lista_padres'),

	url(r'^profesores/$','principal.views.ver_lista_profesores'),

	# Registrar Comunicados
	url(r'^profesor/reg_comunicado/$','principal.views.reg_comunicado'),
	url(r'^ajax/grado_profesores/$','principal.views.ajax_grado_profesores'),
	url(r'^ajax/seccion_profesores/$','principal.views.ajax_seccion_profesores'),
	url(r'^ajax/reg_comunicado/$','principal.views.ajax_reg_comunicado'),	
	#Ver Comunicado Alumnos
	url(r'^alumno/ver_comunicados/$' , 'principal.views.alumno_ver_comunicados'),

	#ADMINNISTRADOR
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Cursos
    url(r'^cursos/$', "principal.views.cursos"),

    # Alumnos
    url(r'^alumnos/$', "principal.views.alumnos"),

    # Probando json y ajax
	url(r'^prueba/$', "principal.views.prueba"),
	url(r'^ajax/prueba/$', "principal.views.ajax_prueba"),    

    # Pagina de inicio (login)
    url(r'^$', "principal.views.inicio"),

    # Cerrar session
    url(r'^cerrar/', "principal.views.cerrar"),
    url(r'^profesor/registrar/$', 'principal.views.registrar_profesor'),

    # Llamados ajax
    url(r'^ajax/alumnos/$', "principal.views.ajax_alumnos"),
    url(r'^ajax/alumnos/2/$', "principal.views.ajax_alumnos_2"),
    url(r'^ajax/secciones/$', "principal.views.ajax_secciones"),
    url(r'^ajax/secciones/3$', "principal.views.ajax_secciones_3"),

    #profesores
    url(r'^profesoress/$', "principal.views.profesores"),
    url(r'^ajax/profesores/2/$', "principal.views.ajax_profesores_2"),
    url(r'^ajax/profesores/$', "principal.views.ajax_profesores"),
	url(r'^ajax/secciones/1/$', "principal.views.ajax_secciones_1"),


	#asistencias
	url(r'^asistencia/$', "principal.views.asistencia"),
	url(r'^ajax/asistencias/2/$', 'principal.views.ajax_asistencias_2'),
    url(r'^ajax/secciones/4$', "principal.views.ajax_secciones_4"),



)

