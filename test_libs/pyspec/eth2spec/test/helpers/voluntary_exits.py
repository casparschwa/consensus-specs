from eth2spec.utils import bls


def sign_voluntary_exit(spec, state, voluntary_exit, privkey):
    domain = spec.get_domain(state, spec.DOMAIN_VOLUNTARY_EXIT, voluntary_exit.epoch)
    message = spec.compute_domain_wrapper_root(voluntary_exit, domain)
    return spec.SignedVoluntaryExit(
        message=voluntary_exit,
        signature=bls.Sign(privkey, message)
    )
