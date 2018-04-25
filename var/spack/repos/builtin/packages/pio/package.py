##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install pio
#
# You can edit this file again by typing:
#
#     spack edit pio
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
import fnmatch, os


#class Pio(Package):
class Pio(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    #url      = "https://github.com/NCAR/ParallelIO/archive/pio1_7_1.tar.gz"
    url      = "https://github.com/NCAR/ParallelIO/archive/pio1_10_0.tar.gz"

    # FIXME: Add proper versions and checksums here.
    #version('1.7.1', 'd5e5e36e5fe5ac05685c069a7e421f5b')
    version('1.10.0', '74bdf5e4abc040fc9e1679095926952f')

    # FIXME: Add dependencies if required.
    depends_on('mpi')
    depends_on('parallel-netcdf')
    depends_on('netcdf-fortran')
    depends_on('netcdf')


#    def install(self, spec, prefix):
#      env['MPICC'] = spec['mpi'].mpicc
#      env['MPICXX'] = spec['mpi'].mpicxx
#      env['MPIFC'] = spec['mpi'].mpifc
#      with working_dir("pio"):
#        configure('NETCDF_PATH=%s' % self.spec['netcdf-fortran'].prefix, 
#                  'PNETCDF_PATH=%s' % self.spec['parallel-netcdf'].prefix,      
#                  '--prefix=%s' % self.spec.prefix)
#        make(parallel=False)
#        make('install')
        
    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        
        options = []
        # specify MPI compilers
        options.extend([
        '-DCMAKE_C_COMPILER=%s'       % self.spec['mpi'].mpicc,
        '-DCMAKE_CXX_COMPILER=%s'     % self.spec['mpi'].mpicxx,
        '-DCMAKE_Fortran_COMPILER=%s' % self.spec['mpi'].mpifc,
        '-DMPI_BASE_DIR:PATH=%s'      % self.spec['mpi'].prefix
        ])

        # dependencies
        options.extend([
        '-DNetCDF_Fortran_PATH=%s' % self.spec['netcdf-fortran'].prefix,
        '-DNetCDF_C_PATH=%s' % self.spec['netcdf'].prefix,
        '-DPnetCDF_PATH=%s' % self.spec['parallel-netcdf'].prefix,
        '-DLIBZ_PATH=%s' % self.spec['zlib'].prefix,
        '-DHDF5_PATH=%s' % self.spec['hdf5'].prefix
        ])

        # add extra tools pio requires :(
        options.extend([
        '-DUSER_CMAKE_MODULE_PATH:LIST=/turquoise/usr/projects/climate/SHARED_CLIMATE/software/source-build/CMake_Fortran_utils',
        '-DGENF90_PATH:LIST=/turquoise/usr/projects/climate/SHARED_CLIMATE/software/source-build/CMake_Fortran_utils'
        ])

        # install prefix
        options.extend(['-DCMAKE_INSTALL_PREFIX:PATH=%s' % self.prefix])

        return options


    # the build process doesn't actually install anything, do it by hand
    def install(self, spec, prefix):
       #mkdir(prefix) # already created by spack
       src = "{0}/spack-build/pio".format(self.stage.source_path)
       print src
       print prefix
       print self.prefix
       files = []
       files = fnmatch.filter(os.listdir(src),'*.mod')
       print files
       files.append('libpio.a')
       print files

       for f in files:
           install(join_path(src, f), join_path(self.prefix, f))
