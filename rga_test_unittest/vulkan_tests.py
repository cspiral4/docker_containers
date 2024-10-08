#
# test descriptions
#
#  {testname: [ shaderfolder, [ cli arg list ], [ test suite list], "test description, can be multi-line"}
#
# shaderfolder is relative to the INPUT_FOLDER parameter
# input file names (vert, frag, tesc, tese, comp) are relative to shaderfolder
# NOTE: help test handled uniquely in test functions
#
vulkan_tests = {
    "test01": [ 'computenbody',
                ['--vert-glsl', 'particle.vert',
                 '--frag-glsl', 'particle.frag',
                 '--comp-glsl', 'particle.comp',
                 '-a',
                 '-b',
                 '-v', '--keep'],
                ['SMOKE', 'VULKAN', 'GLSL', 'POSITIVE', 'REGRESSION'],
                "Verify vert, frag, and comp compilation using computenbody Vulkan shaders"]
    "test02": [ 'bad_folder',
                ['-c', 'gfx1100',
                 '--vert-glsl', 'particle.vert',
                 '--frag-glsl', 'particle.frag',
                 '--comp-glsl', 'particle.comp',
                 '-a', 'computenbody_analysis',
                 '-b', 'computenbody.bin',
                 '-v', '--keep']
                ['SMOKE', 'VULKAN', 'GLSL', 'NEGATIVE', 'REGRESSION'],
                "Verify handling of invalid input file paths" ]
    }

# Default GPUs for test targets.
vulkan_target_gpu = 'gfx1100'
