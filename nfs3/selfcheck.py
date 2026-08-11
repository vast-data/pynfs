#!/usr/bin/env python3
# selfcheck.py - smoke test for the vendored nfs3/NSM/NLM tester.
#
# Verifies the self-contained lib/ imports cleanly and that testmod can
# discover the nfs3 test suite, including the specific codes comet drives
# (NSM*, POSIXACL*, CREATE*, MOUNT_*, RDDIR*, WRITE*). Fails loudly if the
# vendored stack (rpc/nfs3/nlm/nsm/testmod) is broken. No test framework.
#
# Run: python3 nfs3/selfcheck.py
import os
import sys

_here = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, os.path.join(_here, 'lib'))

import testmod
import nfs3.servertests.environment  # noqa: F401  (import must not explode)

tests, fdict, cdict = testmod.createtests(['nfs3.servertests'])
codes = set(cdict.keys())

required = {
    "NSM0", "NSM6",
    "POSIXACL01", "POSIXACL02",
    "CREATE9", "CREATE10",
    "MOUNT_NULL", "MOUNT_MNT_V1", "MOUNT_DUMP", "MOUNT_EXPORT",
    "RDDIR1", "RDDIRPLS1",
    "WRITE1", "WRITEMW1", "WRITEDRC1",
}
missing = sorted(required - codes)
assert not missing, "missing test codes: %s" % missing
assert len(codes) > 40, "suspiciously few test codes discovered: %d" % len(codes)

print("OK: %d nfs3 test codes discovered, all %d required codes present"
      % (len(codes), len(required)))
