import pytest
import graphics.lightfield as mod

CASES = [
    ("microlens_grid_calib", (1,)),
    ("focal_stack_subdivide", (1,)),
    ("view_arrival_fence", (1,)),
    ("per_view_vignette", (1,)),
    ("overlap_exposure_joint", (1,)),
    ("refocus_depth_consistent", (1,)),
    ("load_lightfield", (1,)),
    ("slice_subaparture", (1,)),
    ("refocus_lightfield", (1,)),
    ("present_lightfield", (1,)),
    ("validate_lightfield", (1,)),
    ("metrics_lightfield", (1,)),
    ("audit_lightfield", (1,)),
    ("fallback_lightfield", (1,)),
    ("determinism_lightfield", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
