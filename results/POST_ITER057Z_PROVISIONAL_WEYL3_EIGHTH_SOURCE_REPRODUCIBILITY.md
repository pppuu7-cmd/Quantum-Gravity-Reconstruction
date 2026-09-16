# Post-Iter057Z provisional Weyl3 degree-eight source — reproducibility hashes

Date: 2026-09-16

Research branch certificate parent: `ef393c39e545e8a4d581cd92f43e7d11eabb60f9`.

The computation was executed twice from the working evaluator; both complete result JSON files were byte-identical.

A separate self-contained bundle was then assembled with relative paths, unpacked into a new directory, and executed again. The fresh bundle execution exited with code 0 and its `reproduced_result.json` was byte-identical to the bundled reference result.

Stable hashes:

- complete source canonical serialization: `ab993fd4c987272208831d5c5ff2c24c905d5a11625a65b58fff8012e2c4f828`;
- complete result JSON: `6ef4e67ece3de8b00731c8b37bccca49ec28c99213d61a0ef4f9153daa8a7a1a`;
- degree-eight-only CSV: `76e4f10a8d4533627d83de8f5fc7d5feb99216f924f2c17ed94ccd107ca62d2c`;
- complete even source CSV 0/2/4/6/8: `3a562fe21c3fed1d9756ac97b7abbe79a1fc2031fb574ba4a76b06b6faa34687`;
- independent R12 JSON consumed: `f030a326fe19a289c27fb2617665621dc2124434b61b62812867508323fe1c43`;
- independent Iter057X result consumed for lower replay: `15241042ad0a17ce4c778e19cc18757a185e4bd430e351f4bd9b76965a8c37b7`;
- self-contained reproduction ZIP: `25a2fe01d55186578e82e08823b1342fed8e463408cc5f6cfda9f65f023c4283`.

The bundle-local evaluator differs from the working evaluator only in path resolution and default output location; it uses the same exact tensor algorithm and controls. Its own file SHA-256 is `deed25b77dc5ec9a2aa73b0f1c39d85a514eff1d53f7916214f67fc05cc2ea59`.

This remains provisional rather than canonical because official Iter057Z has not terminalized on `main` as of this certificate. No promotion to an official source gate is authorized until the official canonical R12 authority is consumed and compared.
