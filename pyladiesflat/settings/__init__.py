from split_settings.tools import optional, include

include(
    'base/*.py',
    optional('local/*.py')
)
