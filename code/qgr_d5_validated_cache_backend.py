#!/usr/bin/env python3
"""Validated D5/H5 cache backend for prospectively frozen downstream gates.

This wrapper deliberately reuses the exact build_cache/reduce_cache functions
that were executed in run 34793411230 and terminally classified
D5_CANONICAL_CACHE_EQUIVALENCE_PASS.  It introduces no alternative stencil.
"""
from __future__ import annotations

import numpy as np

import qgr_d5_canonical_cache_equivalence as validated

VALIDATED_HSTEP = 5.0e-4
VALIDATION_RUN = 34793411230
VALIDATION_CLASSIFICATION = "D5_CANONICAL_CACHE_EQUIVALENCE_PASS"
VALIDATION_HEAD = "43b844f691a716c0f678b9ed20c7ddb3fa140140"


def assemble_minus5_cached(metric, x, hstep=VALIDATED_HSTEP):
    h=float(hstep)
    if h != VALIDATED_HSTEP:
        raise ValueError(
            f"validated cache backend is frozen only at h={VALIDATED_HSTEP}; got {h}"
        )
    xx=np.asarray(x,dtype=float)
    cache=validated.build_cache(metric,xx,h)
    if len(cache)!=129:
        raise RuntimeError(f"validated cache lattice must contain 129 unique points, got {len(cache)}")
    H,z=validated.reduce_cache(cache,h)
    nums=[*np.asarray(H).ravel(),*np.asarray(z['D']).ravel(),*np.asarray(z['P']).ravel()]
    if not np.isfinite(nums).all():
        raise RuntimeError("non-finite validated cache output")
    z=dict(z)
    z['validated_cache_unique_points']=len(cache)
    z['validated_cache_run']=VALIDATION_RUN
    z['validated_cache_classification']=VALIDATION_CLASSIFICATION
    z['validated_cache_head']=VALIDATION_HEAD
    return H,z
