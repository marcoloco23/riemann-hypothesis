#!/usr/bin/env bash
set -euo pipefail

repo_slug="${1:-marcoloco23/riemann-hypothesis}"

gh repo edit "$repo_slug" \
  --visibility public \
  --accept-visibility-change-consequences \
  --description "Open, reproducible research on the Riemann hypothesis with explicit evidence states, negative results, and formal-verification plans." \
  --enable-issues=true \
  --enable-discussions=true \
  --enable-projects=true \
  --enable-wiki=false \
  --delete-branch-on-merge=true \
  --allow-squash-merge=true \
  --allow-rebase-merge=true \
  --allow-merge-commit=false

for topic in \
  riemann-hypothesis \
  analytic-number-theory \
  riemann-zeta \
  explicit-formula \
  reproducible-research \
  lean4
do
  gh repo edit "$repo_slug" --add-topic "$topic"
done

while IFS='|' read -r name color description
do
  gh label create "$name" \
    --repo "$repo_slug" \
    --color "$color" \
    --description "$description" \
    --force
done <<'LABELS'
review|5319E7|Independent mathematical review
reproduction|0E8A16|Computational reproduction
proposal|1D76DB|Scoped research proposal
correction|D73A4A|Correction or status downgrade
status: conjectured|FBCA04|Claim is conjectural
status: numerical|C2E0C6|Numerical evidence without a complete certificate
status: proved-written|0052CC|Complete written proof; independent review pending
status: reviewed|0E8A16|Independent human review recorded
status: machine-checked|006B75|Pinned proof-assistant verification
status: refuted|B60205|Claim refuted with recorded evidence
help wanted|008672|Contribution is welcome
good first issue|7057FF|Suitable first contribution
LABELS

printf 'Configured https://github.com/%s\n' "$repo_slug"
