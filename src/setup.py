from setuptools import setup
import setup_translate

pkg = 'Extensions.HbbTV'
setup(name='enigma2-plugin-extensions-hbbtv',
       version='3.0',
       description='HbbTV player',
       package_dir={pkg: 'HbbTV'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
