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


class Pio(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/NCAR/ParallelIO/archive/pio1_7_1.tar.gz"

    # FIXME: Add proper versions and checksums here.
    version('1.7.1', 'd5e5e36e5fe5ac05685c069a7e421f5b')

    # FIXME: Add dependencies if required.
    depends_on('mpi')
    depends_on('parallel-netcdf')
    depends_on('netcdf-fortran')


    def install(self, spec, prefix):
      env['MPICC'] = spec['mpi'].mpicc
      env['MPICXX'] = spec['mpi'].mpicxx
      env['MPIFC'] = spec['mpi'].mpifc
      with working_dir("pio"):
        configure('NETCDF_PATH=%s' % self.spec['netcdf-fortran'].prefix, 
                  'PNETCDF_PATH=%s' % self.spec['parallel-netcdf'].prefix,      
                  '--prefix=%s' % self.spec.prefix)
        make()
        make('install')
