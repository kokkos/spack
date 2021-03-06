# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Xf86driproto(AutotoolsPackage):
    """XFree86 Direct Rendering Infrastructure Extension.

    This extension defines a protocol to allow user applications to access
    the video hardware without requiring data to be passed through the X
    server."""

    homepage = "http://cgit.freedesktop.org/xorg/proto/xf86driproto"
    url      = "https://www.x.org/archive/individual/proto/xf86driproto-2.1.1.tar.gz"

    version('2.1.1', '3ba16a48d8d9f9f746f9bd281ba8fb3f')

    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')
