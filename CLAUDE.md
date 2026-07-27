# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is the course repository for **Introduction to Artificial Intelligence** (Anahuac Mayab University, Prof. Miguel A. Guirao Aguilera). It holds **student-facing activity materials** — assignment notebooks, instructions, starter code, and grading questions — not a software product. Changes here are course content edits, not application features.

## Repository structure

- `activities/ActivityN/` — one folder per activity, each self-contained with its own `README.md` (instructions, grading rubric, submission steps) and, where applicable, `requirements.txt`. Activity numbering follows the course session schedule (see `activities/README.md` for the session-to-activity map), not sequential folder order — Activity8 and Activity10 currently exist as empty placeholders. **Activity numbers have shifted before** (a Sessions 4–6 gap was filled by inserting Activity 3 and Activity 4, cascading every later activity up by 2) — if adding a new activity would require inserting into an already-used number, treat that as a real decision to confirm with the user (full renumber vs. reusing an empty placeholder), not something to guess at silently.
- `activities/README.md` — master index linking every activity to its session numbers and files; keep this in sync when adding/renaming an activity.
- `README.md` (root) — public-facing syllabus-style table of activities with topic/tool summaries; update alongside `activities/README.md` when an activity's scope changes.
- `instructor/` — instructor-only source material (session content, midterm content, per-activity authoring notes). **Gitignored** (see `.gitignore`) — never assume its contents are tracked or will show up in `git status`/`git log`, and don't rely on it being present for another checkout of this repo.
- `.claude/` — also gitignored; local Claude Code settings, not shared with students or other machines.

## Activity content patterns

Four recurring activity shapes exist:

1. **Notebook-based (Activities 9, 11, 12, 13)** — a Jupyter notebook (`AN_*.ipynb`) is the graded deliverable, paired with a `README.md` (setup + grading table) and an `AN_PlotAnalysis_Questions.md` (written-answer questions students submit separately, referencing specific plots/outputs from their executed notebook). All four share the same `pip install -r requirements.txt` + `jupyter notebook AN_*.ipynb` workflow, with `ipywidgets` used for in-notebook interactive experiments. Dataset generation cells use a fixed random seed and must not be modified by students — grading assumes every student's notebook is running on identical data. Activity 4 is a lighter variant of this pattern: a single comprehension-lab notebook with no dataset, no plots file, and no extra `requirements.txt` (it deliberately only needs the standard library and the `ai_uam` environment from Activity 2).
2. **Markdown-assignment-based (Activities 5, 6, 7)** — no notebook; each session's assignment is its own `Assignment_N_*.md` file with no separate grading rubric file. Activity 7 additionally ships runnable Python scripts (`bfs_search.py`, `greedy_search.py`, `graph_generator.py`) plus a `STUDENT_GUIDE_Running_Code.md` walking students through CLI usage, e.g.:
   ```bash
   python bfs_search.py <graph_size> <search_property> <search_value>
   python greedy_search.py <graph_size> <start_node> <goal_node>
   ```
   Graphs are pre-generated JSON files (see `graphs.zip`); `graph_generator.py` is how they were produced, not something students normally re-run.
3. **Team PPT + English video (Activities 1, 3)** — no code, no notebook. Teams of 2–3 present an 8–10 slide deck plus a 5–7 minute English-language video. Each ships a companion "brief" document establishing fixed, gradable facts (`A1_CompanyBrief.md` for a fictional client scenario; `A3_DomainOptions.md` for a menu of real-world domains — Activity 1 uses one shared fictional scenario, Activity 3 deliberately uses real applications/real law instead since its source sessions survey real industries and real regulation) and a phase-by-phase `A*_PresentationGuide.md` for building the slides/video.
4. Activity 14 is a fifth, distinct pattern: no code or notebook at all — students use Claude.ai itself as the deliverable-building tool against a fictional company brief (`A14_CompanyBrief.md`) and a prompting guide (`A14_PromptingGuide.md`), submitting a website plus their chat transcript and a reflection essay.

## Fictional scenarios reused across activities

Several activities share a running fictional-client narrative that gives assignments continuity (MRHA CardioWatch appears in both Activity 9 and Activity 11). When editing or extending an activity, check sibling activities for scenario/persona consistency before inventing a new one.

## Working conventions

- There is no build/lint/test tooling for this repo — "testing" a change means executing the affected notebook top-to-bottom and confirming cells run without modifying the seeded data-generation cell, or running the Activity 7 scripts against the sample graphs.
- Each activity's `requirements.txt` is independent (no shared root-level requirements file); update the specific activity's file if its notebook's dependencies change.
- Grading rubrics live inline in each activity's `README.md` as a point-value table — keep point totals summing to 100 when editing.
