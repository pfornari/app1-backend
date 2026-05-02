from django.core.management.base import BaseCommand
from django.utils import timezone
from catalogos.models import Pais, Provincia, Estado, TipoUnidad, Unidad


class Command(BaseCommand):
    help = 'Importa los datos semilla del sistema SAGTA original'

    def handle(self, *args, **options):
        self.stdout.write('Importando datos semilla...')

        self._importar_pais()
        self._importar_provincias()
        self._importar_estados()
        self._importar_tipo_unidades()
        self._importar_unidades()

        self.stdout.write(self.style.SUCCESS('Datos semilla importados correctamente.'))

    def _importar_pais(self):
        Pais.objects.get_or_create(
            pais_id=1,
            defaults={
                'pais_nombre': 'Argentina',
                'fecha_alta': timezone.now(),
            }
        )
        self.stdout.write('  ✓ País')

    def _importar_provincias(self):
        provincias = [
            (1, 'Buenos Aires'), (2, 'Catamarca'), (3, 'Chaco'),
            (4, 'Chubut'), (5, 'Córdoba'), (6, 'Corrientes'),
            (7, 'Entre Ríos'), (8, 'Formosa'), (9, 'Jujuy'),
            (10, 'La Pampa'), (11, 'La Rioja'), (12, 'Mendoza'),
            (13, 'Misiones'), (14, 'Neuquén'), (15, 'Río Negro'),
            (16, 'Salta'), (17, 'San Juan'), (18, 'San Luis'),
            (19, 'Santa Cruz'), (20, 'Santa Fe'), (21, 'Santiago del Estero'),
            (22, 'Tierra del Fuego'), (23, 'Tucumán'),
            (24, 'Ciudad Autónoma de Buenos Aires'),
        ]
        pais = Pais.objects.get(pais_id=1)
        for prvi_id, nombre in provincias:
            Provincia.objects.get_or_create(
                prvi_id=prvi_id,
                defaults={
                    'pais': pais,
                    'prvi_nombre': nombre,
                    'fecha_alta': timezone.now(),
                }
            )
        self.stdout.write('  ✓ Provincias')

    def _importar_estados(self):
        estados = [
            (1,  'T', 'Ternero/a',         '#FFFFFF', 'VP'),
            (2,  'N', 'Vaquilla/Novillo',   '#FFFFFF', 'VP'),
            (3,  'V', 'Vendida',            '#FF0000', 'VP'),
            (4,  'S', 'En Servicio',        '#3399FF', 'VP'),
            (5,  'P', 'Preñada',            '#66FFFF', 'VP'),
            (6,  'E', 'En Producción',      '#66FF00', 'VP'),
            (7,  'C', 'Con Cría',           '#00FFFF', 'VP'),
            (8,  'M', 'Muerta',             '#000000', 'VP'),
            (11, 'N', 'No Productiva',      '#FFFF66', 'VR'),
            (12, 'P', 'Produciendo',        '#FFFF66', 'VR'),
            (13, 'S', 'Seca',               '#FFFF00', 'VR'),
        ]
        for esta_id, ident, nombre, color, uso in estados:
            Estado.objects.get_or_create(
                esta_id=esta_id,
                defaults={
                    'esta_identificador': ident,
                    'esta_nombre': nombre,
                    'esta_color': color,
                    'esta_uso': uso,
                }
            )
        self.stdout.write('  ✓ Estados')

    def _importar_tipo_unidades(self):
        tipos = [
            (1, 'Peso'),
            (2, 'Volumen'),
            (3, 'Superficie'),
        ]
        for tiun_id, nombre in tipos:
            TipoUnidad.objects.get_or_create(
                tiun_id=tiun_id,
                defaults={
                    'tiun_nombre': nombre,
                    'fecha_alta': timezone.now(),
                }
            )
        self.stdout.write('  ✓ Tipos de Unidad')

    def _importar_unidades(self):
        unidades = [
            (1, 1, 'Kilogramo'),
            (2, 1, 'Gramo'),
            (3, 1, 'Tonelada'),
            (4, 2, 'Litro'),
            (5, 2, 'Mililitro'),
            (6, 3, 'Hectárea'),
            (7, 3, 'Metro cuadrado'),
        ]
        for unid_id, tiun_id, nombre in unidades:
            Unidad.objects.get_or_create(
                unid_id=unid_id,
                defaults={
                    'tipo_unidad_id': tiun_id,
                    'unid_nombre': nombre,
                    'fecha_alta': timezone.now(),
                }
            )
        self.stdout.write('  ✓ Unidades')