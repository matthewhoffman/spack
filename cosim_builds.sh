
# Set clean path
export PATH=/usr/lib64/qt-3.3/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/usr/projects/ic/usr/bin

export SPACK_ROOT=/usr/projects/climate/SHARED_CLIMATE/software/source-build/spack
export PATH=$SPACK_ROOT/bin:$PATH
module purge
module load gcc/6.4.0
module load openmpi/2.1.2
module load cmake


# Getting needed packages
# -----------------------
# This only needs to be done once for each package.
# most packages will not download successfully through HPC firewall, so you have manually download them 
# to your local machine and ssh to /usr/projects/climate/SHARED_CLIMATE/software/source-build/spack/var/spack/cache/, 
# e.g.: /usr/projects/climate/SHARED_CLIMATE/software/source-build/spack/var/spack/cache/parmetis/parmetis-4.0.3.tar.gz
# Actually, the better method is to make a local clone of spack on your local machine with internet access.
# Then make a mirror of all the packages you will need:
# spack mirror create bzip2 zlib netcdf netcdf-fortran hdf5 metis parmetis boost parallel-netcdf
# You can specify version if needed: http://spack.readthedocs.io/en/latest/mirrors.html?highlight=fetch#spack-mirror
# Then scp the whole mirror to Turquoise.
# Then add the mirror on Turquoise:
# spack mirror add local_filesystem file://turquoise/usr/projects/climate/SHARED_CLIMATE/software/source-build/build_sandbox/spack-mirror


# Setup config, compilers, packages.  See git history of this branch for examples.

# Now install desired packages:
#spack install metis
#spack install parmetis
#spack install boost+mpi
###spack install  hdf5+mpi  # for some reason netcdf will not use this :( but it installs its own

#spack install netcdf ^hdf5+mpi
#spack install netcdf-fortran^hdf5+mpi
#spack install parallel-netcdf
#spack install pio
