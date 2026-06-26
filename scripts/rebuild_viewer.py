#!/usr/bin/env python3
"""
Regenerate viewer index.html and pre-rendered.html with a stunning, premium
Vanilla CSS & JS interface, embedding the full CEFR, American, and Discrepancies databases.
"""
import json
import os

DATA = "/root/projects/english-grammar-db/data"
INDEX_OUT = "/root/projects/english-grammar-db/viewer/index.html"
PRERENDER_OUT = "/root/projects/english-grammar-db/viewer/pre-rendered.html"

with open(f"{DATA}/english_grammar_cefr.json", "r", encoding="utf-8") as f:
    cefr = json.load(f)
with open(f"{DATA}/english_grammar_american.json", "r", encoding="utf-8") as f:
    am = json.load(f)
with open(f"{DATA}/english_grammar_bre_ame_discrepancies.json", "r", encoding="utf-8") as f:
    disc = json.load(f)

# Serialize JSON to insert into JavaScript
cefr_js = json.dumps(cefr, ensure_ascii=False)
am_js = json.dumps(am, ensure_ascii=False)
disc_js = json.dumps(disc, ensure_ascii=False)

# Let's count totals
cefr_gr = sum(len(s["points"]) for l in cefr["levels"].values() for c in l["categories"] for s in c["subs"])
ame_gr = sum(len(s["points"]) for l in am["levels"].values() for c in l["categories"] for s in c["subs"])
disc_total = sum(len(c["items"]) for c in disc["categories"])

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>English Grammar Database — Interactive Explorer</title>
  <meta name="description" content="Explore a complete hierarchical database of English grammar points mapped to CEFR (A1-C2) and American ESL (L1-L6) standards, including British vs American grammatical discrepancies.">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --bg-primary: #060913;
      --bg-secondary: #0b1120;
      --bg-tertiary: #131c31;
      --bg-glass: rgba(11, 17, 32, 0.65);
      --border-color: rgba(255, 255, 255, 0.08);
      --border-color-glow: rgba(99, 102, 241, 0.25);
      
      --text-primary: #f3f4f6;
      --text-secondary: #9ca3af;
      --text-muted: #6b7280;
      
      --accent-primary: #6366f1;
      --accent-primary-hover: #4f46e5;
      --accent-secondary: #10b981;
      --accent-rose: #f43f5e;
      --accent-purple: #8b5cf6;
      --accent-amber: #f59e0b;
      --accent-orange: #f97316;
      
      --font-headings: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      
      --transition-fast: 0.15s ease;
      --transition-normal: 0.3s cubic-bezier(0.16, 1, 0.3, 1);

      --cefr-c0: #6366f1;
      --cefr-c1: #10b981;
      --cefr-c2: #eab308;
      --cefr-c3: #f97316;
      --cefr-c4: #8b5cf6;
      --cefr-c5: #ec4899;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: var(--font-body);
      background-color: var(--bg-primary);
      color: var(--text-primary);
      height: 100vh;
      overflow: hidden;
      position: relative;
    }

    /* Ambient glowing orbs in background */
    .glow-orb {
      position: absolute;
      border-radius: 50%;
      filter: blur(140px);
      z-index: 0;
      opacity: 0.08;
      pointer-events: none;
    }
    .orb-1 {
      width: 500px;
      height: 500px;
      background: var(--accent-primary);
      top: -150px;
      left: -100px;
    }
    .orb-2 {
      width: 600px;
      height: 600px;
      background: var(--accent-purple);
      bottom: -200px;
      right: -100px;
    }

    /* Application wrapper */
    .app-container {
      position: relative;
      z-index: 10;
      display: flex;
      height: 100vh;
      width: 100vw;
      backdrop-filter: blur(8px);
    }

    /* Sidebar */
    .sidebar {
      width: 350px;
      min-width: 350px;
      background-color: var(--bg-secondary);
      border-right: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      height: 100%;
      padding: 24px;
      overflow-y: auto;
    }

    .app-branding {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 24px;
    }
    .app-icon {
      width: 38px;
      height: 38px;
      border-radius: 10px;
      background: linear-gradient(135deg, var(--accent-primary), var(--accent-purple));
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 20px rgba(99, 102, 241, 0.35);
    }
    .app-icon svg {
      width: 22px;
      height: 22px;
      fill: #fff;
    }
    .app-title-container {
      display: flex;
      flex-direction: column;
    }
    .app-title {
      font-family: var(--font-headings);
      font-size: 19px;
      font-weight: 800;
      letter-spacing: -0.5px;
      background: linear-gradient(to right, #ffffff, #d1d5db);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .app-subtitle {
      font-size: 11px;
      color: var(--text-secondary);
    }

    /* Stats Widget */
    .stats-card {
      background-color: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 16px;
      margin-bottom: 24px;
    }
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-bottom: 12px;
    }
    .stat-item {
      display: flex;
      flex-direction: column;
    }
    .stat-num {
      font-family: var(--font-headings);
      font-size: 20px;
      font-weight: 700;
      color: var(--text-primary);
    }
    .stat-lbl {
      font-size: 10px;
      color: var(--text-secondary);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .stats-progress-container {
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-top: 8px;
    }
    .stats-progress-row {
      display: flex;
      justify-content: space-between;
      font-size: 10px;
      color: var(--text-secondary);
    }
    .stats-progress-bar {
      height: 4px;
      background-color: rgba(255, 255, 255, 0.06);
      border-radius: 2px;
      overflow: hidden;
    }
    .stats-progress-fill {
      height: 100%;
      border-radius: 2px;
      background: linear-gradient(to right, var(--accent-primary), var(--accent-purple));
      width: 100%;
      transition: width var(--transition-normal);
    }

    /* System Tabs Switcher */
    .tab-switcher {
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-bottom: 24px;
    }
    .tab-btn {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 12px 16px;
      background-color: transparent;
      border: 1px solid transparent;
      border-radius: 10px;
      color: var(--text-secondary);
      cursor: pointer;
      text-align: left;
      font-family: var(--font-headings);
      font-size: 13px;
      font-weight: 600;
      transition: all var(--transition-fast);
      width: 100%;
    }
    .tab-btn:hover {
      background-color: rgba(255, 255, 255, 0.03);
      color: var(--text-primary);
    }
    .tab-btn.active {
      background-color: rgba(99, 102, 241, 0.08);
      border-color: var(--border-color-glow);
      color: var(--text-primary);
    }
    .tab-btn svg {
      width: 18px;
      height: 18px;
      color: var(--text-secondary);
      transition: color var(--transition-fast);
    }
    .tab-btn.active svg {
      color: var(--accent-primary);
    }
    .tab-badge {
      margin-left: auto;
      font-size: 10px;
      padding: 2px 6px;
      border-radius: 6px;
      background-color: rgba(255, 255, 255, 0.06);
      color: var(--text-secondary);
    }
    .tab-btn.active .tab-badge {
      background-color: rgba(99, 102, 241, 0.2);
      color: #a5b4fc;
    }

    /* Level Selector Grid */
    .level-selector-section {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-bottom: 24px;
    }
    .level-selector-title {
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--text-muted);
      letter-spacing: 1px;
    }
    .level-selector-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 6px;
    }
    .level-btn {
      padding: 8px 4px;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      background-color: transparent;
      color: var(--text-secondary);
      font-family: var(--font-headings);
      font-size: 11px;
      font-weight: 700;
      text-align: center;
      cursor: pointer;
      transition: all var(--transition-fast);
    }
    .level-btn:hover {
      border-color: rgba(255, 255, 255, 0.15);
      color: var(--text-primary);
    }
    .level-btn.active {
      color: #fff;
      border-color: transparent;
      box-shadow: 0 0 12px var(--level-color-alpha, rgba(99,102,241,0.25));
    }
    .level-btn.active-cefr-0 { background: var(--cefr-c0); }
    .level-btn.active-cefr-1 { background: var(--cefr-c1); }
    .level-btn.active-cefr-2 { background: var(--cefr-c2); }
    .level-btn.active-cefr-3 { background: var(--cefr-c3); }
    .level-btn.active-cefr-4 { background: var(--cefr-c4); }
    .level-btn.active-cefr-5 { background: var(--cefr-c5); }

    /* Quick Tags */
    .quick-nav-section {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-top: auto;
      padding-top: 20px;
      border-top: 1px solid var(--border-color);
    }
    .quick-nav-title {
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--text-muted);
      letter-spacing: 1px;
    }
    .quick-nav-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }
    .nav-tag {
      font-size: 10px;
      font-weight: 600;
      padding: 5px 10px;
      border-radius: 20px;
      background-color: rgba(255, 255, 255, 0.03);
      color: var(--text-secondary);
      cursor: pointer;
      border: 1px solid transparent;
      transition: all var(--transition-fast);
    }
    .nav-tag:hover {
      background-color: rgba(255, 255, 255, 0.08);
      color: var(--text-primary);
      border-color: rgba(255, 255, 255, 0.1);
    }
    .nav-tag.syntax { border-color: rgba(99, 102, 241, 0.2); color: #a5b4fc; }
    .nav-tag.irregular { border-color: rgba(244, 63, 94, 0.2); color: #fda4af; }
    .nav-tag.phrasal { border-color: rgba(16, 185, 129, 0.2); color: #6ee7b7; }

    /* Main Area */
    .main-content {
      flex: 1;
      display: flex;
      flex-direction: column;
      height: 100%;
      background-color: var(--bg-primary);
    }

    /* Sticky Header */
    .main-header {
      padding: 24px;
      background-color: rgba(6, 9, 19, 0.7);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      gap: 16px;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 20;
    }
    .search-wrapper {
      flex: 1;
      position: relative;
    }
    .search-input {
      width: 100%;
      padding: 12px 16px 12px 42px;
      background-color: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      color: var(--text-primary);
      font-family: var(--font-body);
      font-size: 14px;
      transition: all var(--transition-fast);
    }
    .search-input:focus {
      outline: none;
      background-color: rgba(255, 255, 255, 0.05);
      border-color: var(--accent-primary);
      box-shadow: 0 0 15px rgba(99, 102, 241, 0.15);
    }
    .search-icon {
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      width: 18px;
      height: 18px;
      color: var(--text-secondary);
      pointer-events: none;
    }
    .search-shortcut {
      position: absolute;
      right: 14px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 10px;
      padding: 2px 6px;
      background-color: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 4px;
      color: var(--text-secondary);
      pointer-events: none;
    }
    .results-counter {
      font-size: 13px;
      color: var(--text-secondary);
      white-space: nowrap;
    }
    .header-actions {
      display: flex;
      gap: 8px;
    }
    .header-btn {
      padding: 10px 16px;
      background-color: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      color: var(--text-primary);
      font-family: var(--font-headings);
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all var(--transition-fast);
    }
    .header-btn:hover {
      background-color: rgba(255, 255, 255, 0.06);
      border-color: rgba(255, 255, 255, 0.15);
    }

    /* Content tree container */
    .tree-container {
      flex: 1;
      overflow-y: auto;
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    /* Card structures for tree */
    .level-card {
      background-color: rgba(255, 255, 255, 0.01);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      overflow: hidden;
      transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
    }
    .level-card:hover {
      border-color: rgba(255, 255, 255, 0.12);
      box-shadow: 0 4px 25px rgba(0, 0, 0, 0.25);
    }
    .level-header {
      padding: 16px 20px;
      background-color: rgba(255, 255, 255, 0.02);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      cursor: pointer;
      user-select: none;
      border-left: 4px solid var(--level-color);
    }
    .chevron-icon {
      width: 14px;
      height: 14px;
      color: var(--text-secondary);
      margin-right: 12px;
      transition: transform 0.2s ease;
    }
    .chevron-icon.open {
      transform: rotate(90deg);
    }
    .level-icon {
      font-size: 18px;
      margin-right: 12px;
    }
    .level-title-wrapper {
      display: flex;
      flex-direction: column;
    }
    .level-name {
      font-family: var(--font-headings);
      font-size: 15px;
      font-weight: 700;
      color: var(--text-primary);
    }
    .level-desc {
      font-size: 11px;
      color: var(--text-secondary);
      margin-top: 2px;
    }
    .level-badge {
      margin-left: auto;
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 20px;
      background-color: var(--level-color-alpha);
      color: var(--level-color);
      border: 1px solid var(--level-color-alpha-border);
    }

    .level-body {
      padding: 8px 0;
      display: flex;
      flex-direction: column;
      background-color: rgba(0, 0, 0, 0.15);
    }
    .level-body.collapsed {
      display: none;
    }

    /* Category folders */
    .cat-node {
      margin: 6px 20px;
      border-radius: 8px;
      overflow: hidden;
    }
    .cat-header {
      padding: 10px 16px;
      display: flex;
      align-items: center;
      cursor: pointer;
      border-radius: 8px;
      background-color: rgba(255, 255, 255, 0.01);
      transition: all var(--transition-fast);
    }
    .cat-header:hover {
      background-color: rgba(255, 255, 255, 0.04);
    }
    .cat-icon {
      font-size: 14px;
      margin-right: 10px;
      color: var(--accent-primary);
    }
    .cat-title {
      font-family: var(--font-headings);
      font-size: 13px;
      font-weight: 600;
      color: var(--text-primary);
    }
    .cat-count {
      margin-left: auto;
      font-size: 10px;
      color: var(--text-muted);
      background-color: rgba(255, 255, 255, 0.03);
      padding: 2px 6px;
      border-radius: 4px;
    }
    .cat-body {
      padding-left: 18px;
      border-left: 1px dashed rgba(255, 255, 255, 0.06);
      margin-left: 22px;
      margin-top: 4px;
      margin-bottom: 4px;
    }
    .cat-body.collapsed {
      display: none;
    }

    /* Subcategories */
    .sub-node {
      margin: 4px 0;
    }
    .sub-header {
      padding: 8px 12px;
      display: flex;
      align-items: center;
      cursor: pointer;
      border-radius: 6px;
      transition: all var(--transition-fast);
    }
    .sub-header:hover {
      background-color: rgba(255, 255, 255, 0.03);
    }
    .sub-icon {
      font-size: 13px;
      margin-right: 8px;
      color: var(--accent-purple);
    }
    .sub-title {
      font-size: 12px;
      font-weight: 500;
      color: var(--text-primary);
    }
    .sub-body {
      padding-left: 14px;
      border-left: 1px dashed rgba(255, 255, 255, 0.06);
      margin-left: 18px;
      margin-top: 2px;
      margin-bottom: 4px;
    }
    .sub-body.collapsed {
      display: none;
    }

    /* Points */
    .point-node {
      padding: 8px 12px;
      border-radius: 6px;
      margin: 2px 0;
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 12px;
      line-height: 1.5;
      color: var(--text-secondary);
      transition: all var(--transition-fast);
    }
    .point-node:hover {
      background-color: rgba(255, 255, 255, 0.02);
      color: var(--text-primary);
    }
    .point-bullet {
      color: var(--text-muted);
      margin-top: 3px;
      font-size: 9px;
    }
    .point-text {
      flex: 1;
    }

    /* Search highlighting */
    .search-highlight {
      background-color: rgba(245, 158, 11, 0.22);
      border-bottom: 2px solid var(--accent-amber);
      color: #fff;
      font-weight: 600;
      border-radius: 2px;
      padding: 0 2px;
    }

    /* Clickable discrepancy tag */
    .ba-tag {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 10px;
      font-weight: 700;
      padding: 1px 6px;
      border-radius: 4px;
      background-color: rgba(244, 63, 94, 0.12);
      color: #fda4af;
      border: 1px solid rgba(244, 63, 94, 0.2);
      cursor: pointer;
      margin-left: 6px;
      transition: all var(--transition-fast);
      vertical-align: middle;
    }
    .ba-tag:hover {
      background-color: var(--accent-rose);
      color: #fff;
      box-shadow: 0 0 8px rgba(244, 63, 94, 0.4);
    }
    .flag-icon {
      font-size: 10px;
    }

    /* Drawer overlay backdrop */
    .backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background-color: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(4px);
      z-index: 90;
      display: none;
      opacity: 0;
      transition: opacity 0.3s ease;
    }
    .backdrop.active {
      display: block;
      opacity: 1;
    }

    /* Comparative slide-over drawer */
    .drawer {
      position: fixed;
      top: 0;
      right: -480px;
      width: 480px;
      max-width: 100vw;
      height: 100vh;
      background-color: #0c1221;
      border-left: 1px solid var(--border-color);
      box-shadow: -10px 0 40px rgba(0, 0, 0, 0.6);
      z-index: 100;
      display: flex;
      flex-direction: column;
      transition: right var(--transition-normal);
    }
    .drawer.open {
      right: 0;
    }
    .drawer-header {
      padding: 24px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .drawer-title-container {
      display: flex;
      flex-direction: column;
      gap: 4px;
      flex: 1;
      margin-right: 16px;
    }
    .drawer-tag-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 4px;
    }
    .drawer-badge {
      font-family: var(--font-headings);
      font-size: 11px;
      font-weight: 800;
      color: var(--accent-rose);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      background-color: rgba(244, 63, 94, 0.12);
      padding: 2px 8px;
      border-radius: 4px;
      border: 1px solid rgba(244, 63, 94, 0.2);
    }
    .drawer-copy-btn {
      font-size: 10px;
      color: var(--text-secondary);
      background: transparent;
      border: none;
      cursor: pointer;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .drawer-copy-btn:hover {
      color: #fff;
    }
    .drawer-title {
      font-family: var(--font-headings);
      font-size: 15px;
      font-weight: 700;
      color: var(--text-primary);
      line-height: 1.4;
    }
    .drawer-close-btn {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background-color: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all var(--transition-fast);
      flex-shrink: 0;
    }
    .drawer-close-btn:hover {
      background-color: rgba(255, 255, 255, 0.08);
      color: #fff;
    }

    .drawer-body {
      flex: 1;
      overflow-y: auto;
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    /* Drawer section layouts */
    .comp-grid {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .comp-card {
      padding: 16px;
      border-radius: 12px;
      border: 1px solid var(--border-color);
    }
    .comp-card.bre {
      border-left: 4px solid var(--accent-primary);
      background-color: rgba(99, 102, 241, 0.03);
    }
    .comp-card.ame {
      border-left: 4px solid var(--accent-orange);
      background-color: rgba(249, 115, 22, 0.03);
    }
    .comp-card-header {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
      font-family: var(--font-headings);
      font-size: 12px;
      font-weight: 700;
    }
    .comp-card-body {
      font-size: 12.5px;
      line-height: 1.5;
      color: var(--text-secondary);
    }

    .ex-section {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .section-title {
      font-family: var(--font-headings);
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--text-muted);
      letter-spacing: 0.8px;
    }
    .ex-box {
      background-color: #070b16;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 12px 16px;
      font-family: var(--font-mono);
      font-size: 11px;
      line-height: 1.6;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .ex-line {
      color: var(--text-secondary);
    }

    .kd-card {
      padding: 16px;
      border-radius: 12px;
      background-color: rgba(245, 158, 11, 0.03);
      border: 1px solid rgba(245, 158, 11, 0.15);
      border-left: 4px solid var(--accent-amber);
    }
    .kd-title-row {
      display: flex;
      align-items: center;
      gap: 8px;
      color: #f59e0b;
      font-family: var(--font-headings);
      font-size: 12px;
      font-weight: 700;
      margin-bottom: 6px;
    }
    .kd-text {
      font-size: 12.5px;
      line-height: 1.5;
      color: var(--text-secondary);
    }

    .meta-row {
      display: flex;
      gap: 12px;
      font-size: 11px;
      color: var(--text-muted);
      margin-top: auto;
      padding-top: 16px;
      border-top: 1px solid var(--border-color);
    }

    /* Scrollbars */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: var(--bg-primary);
    }
    ::-webkit-scrollbar-thumb {
      background: var(--border-color);
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: var(--text-muted);
    }

    /* Responsive */
    @media (max-width: 1024px) {
      .app-container {
        flex-direction: column;
      }
      .sidebar {
        width: 100%;
        min-width: 100%;
        height: auto;
        max-height: 380px;
        border-right: none;
        border-bottom: 1px solid var(--border-color);
      }
      .main-header {
        padding: 16px 24px;
      }
    }
    @media (max-width: 768px) {
      .sidebar {
        max-height: 320px;
        padding: 16px;
      }
      .level-selector-grid {
        grid-template-columns: repeat(3, 1fr);
      }
      .drawer {
        width: 100vw;
      }
    }
  </style>
</head>
<body>
  <!-- Canvas Glowing Orbs -->
  <div class="glow-orb orb-1"></div>
  <div class="glow-orb orb-2"></div>

  <div class="app-container">
    <!-- Sidebar -->
    <aside class="sidebar">
      <div class="app-branding">
        <div class="app-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
          </svg>
        </div>
        <div class="app-title-container">
          <span class="app-title">GrammarDB</span>
          <span class="app-subtitle">Interactive Curricula & Differences</span>
        </div>
      </div>

      <!-- Stats Widget -->
      <div class="stats-card">
        <div class="stats-grid">
          <div class="stat-item">
            <span class="stat-num" id="statTotal">0</span>
            <span class="stat-lbl">Grand Total</span>
          </div>
          <div class="stat-item">
            <span class="stat-num" id="statDisc">0</span>
            <span class="stat-lbl">Discrepancies</span>
          </div>
        </div>
        <div class="stats-progress-container">
          <div class="stats-progress-row">
            <span>CEFR Syllabus: <strong id="statCefr">0</strong></span>
            <span>American: <strong id="statAmerican">0</strong></span>
          </div>
          <div class="stats-progress-bar">
            <div class="stats-progress-fill" id="statProgressFill"></div>
          </div>
        </div>
      </div>

      <!-- Navigation Tabs -->
      <div class="tab-switcher">
        <button class="tab-btn active" data-sys="CEFR" onclick="switchSystem('CEFR')">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
          </svg>
          🇪🇺 CEFR Syllabus
          <span class="tab-badge">{{CEFR_COUNT}}</span>
        </button>
        <button class="tab-btn" data-sys="American" onclick="switchSystem('American')">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 2L2 7l10 5 10-5-10-5z"></path>
            <path d="M2 17l10 5 10-5"></path>
            <path d="M2 12l10 5 10-5"></path>
          </svg>
          🇺🇸 American ESL
          <span class="tab-badge">{{AME_COUNT}}</span>
        </button>
        <button class="tab-btn" data-sys="Discrepancies" onclick="switchSystem('Discrepancies')">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="18" y1="20" x2="18" y2="10"></line>
            <line x1="12" y1="20" x2="12" y2="4"></line>
            <line x1="6" y1="20" x2="6" y2="14"></line>
          </svg>
          🔬 BrE vs AmE
          <span class="tab-badge">{{DISC_COUNT}}</span>
        </button>
      </div>

      <!-- Level Selector section -->
      <div class="level-selector-section" id="levelSelectorSection">
        <span class="level-selector-title">Filter by Level</span>
        <div class="level-selector-grid" id="levelSelectorGrid">
          <!-- Populated dynamically -->
        </div>
      </div>

      <!-- Quick Jumps -->
      <div class="quick-nav-section" id="quickNavSection">
        <span class="quick-nav-title">Quick Syllabus Jumps</span>
        <div class="quick-nav-tags">
          <span class="nav-tag syntax" onclick="jumpToCategory('Syntax')">🔷 Syntax</span>
          <span class="nav-tag irregular" onclick="jumpToCategory('Irregular')">🔄 Irregular Verbs</span>
          <span class="nav-tag phrasal" onclick="jumpToCategory('Phrasal')">📝 Phrasal Verbs</span>
          <span class="nav-tag" onclick="jumpToCategory('Modals')">Modals</span>
          <span class="nav-tag" onclick="jumpToCategory('Present')">Present</span>
          <span class="nav-tag" onclick="jumpToCategory('Future')">Future</span>
        </div>
      </div>
    </aside>

    <!-- Main Content Area -->
    <main class="main-content">
      <!-- Sticky Header -->
      <header class="main-header">
        <div class="search-wrapper">
          <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <input id="searchInput" class="search-input" placeholder="Search grammar point, category, discrepancy...">
          <span class="search-shortcut">/</span>
        </div>
        <span class="results-counter" id="resultsCount">0 results</span>
        <div class="header-actions">
          <button class="header-btn" onclick="expandAll()">📂 Expand All</button>
          <button class="header-btn" onclick="collapseAll()">📁 Collapse All</button>
        </div>
      </header>

      <!-- Cascading Tree Explorer -->
      <div class="tree-container" id="treeContainer">
        <!-- Rendered dynamically -->
      </div>
    </main>

    <!-- Discrepancy Detail Drawer -->
    <div class="backdrop" id="drawerBackdrop" onclick="closeDrawer()"></div>
    <div class="drawer" id="discrepancyDrawer">
      <div class="drawer-header">
        <div class="drawer-title-container">
          <div class="drawer-tag-row">
            <span class="drawer-badge" id="drawerBadge">BA-000</span>
            <button class="drawer-copy-btn" id="drawerCopyBtn" onclick="copyDiscrepancyToClipboard()">
              <svg style="width:12px;height:12px" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
              </svg>
              Copy Details
            </button>
          </div>
          <span class="drawer-title" id="drawerTitle">Point Title</span>
        </div>
        <button class="drawer-close-btn" onclick="closeDrawer()">✕</button>
      </div>
      
      <div class="drawer-body">
        <!-- Comparison Cards -->
        <div class="comp-grid">
          <div class="comp-card bre">
            <div class="comp-card-header">
              <span>🇬🇧 British English (BrE)</span>
            </div>
            <div class="comp-card-body" id="breContent">
              British details.
            </div>
          </div>
          
          <div class="comp-card ame">
            <div class="comp-card-header">
              <span>🇺🇸 American English (AmE)</span>
            </div>
            <div class="comp-card-body" id="ameContent">
              American details.
            </div>
          </div>
        </div>

        <!-- Examples section -->
        <div class="ex-section">
          <span class="section-title">Comparative Examples</span>
          <div class="ex-box" id="examplesContainer">
            <!-- Populated dynamically -->
          </div>
        </div>

        <!-- Key Difference section -->
        <div class="kd-card" id="keyDiffSection">
          <div class="kd-title-row">
            <svg style="width:14px;height:14px" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="12" y1="16" x2="12" y2="12"></line>
              <line x1="12" y1="8" x2="12.01" y2="8"></line>
            </svg>
            <span>Key Divergence Note</span>
          </div>
          <div class="kd-text" id="keyDiffContent">
            Detail key difference.
          </div>
        </div>

        <!-- Metadata Level Reference -->
        <div class="meta-row">
          <span id="metaLevels">Levels</span>
        </div>
      </div>
    </div>
  </div>

  <script>
    // Databases injected from python script
    const CEFR_DB = {{CEFR_DATA}};
    const AMERICAN_DB = {{AMERICAN_DATA}};
    const DISCREPANCIES_DB = {{DISCREPANCIES_DATA}};

    // State management
    let activeSystem = 'CEFR';
    let searchQuery = '';
    let activeLevelFilter = 'all';
    const expandedPaths = new Set();

    // Constant colors
    const LEVEL_COLORS = [
      '#6366f1', // Indigo
      '#10b981', // Emerald
      '#eab308', // Amber
      '#f97316', // Orange
      '#8b5cf6', // Purple
      '#ec4899'  // Pink
    ];

    function getLevelColor(index) {
      return LEVEL_COLORS[index % LEVEL_COLORS.length];
    }

    function getLevelColorAlpha(index, alpha) {
      const hex = getLevelColor(index);
      const r = parseInt(hex.slice(1, 3), 16);
      const g = parseInt(hex.slice(3, 5), 16);
      const b = parseInt(hex.slice(5, 7), 16);
      return `rgba(${r}, ${g}, ${b}, ${alpha})`;
    }

    // Utilities
    function escapeHtml(str) {
      if (!str) return '';
      return str.toString()
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }

    function escapeRegExp(string) {
      return string.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&');
    }

    // Initializer
    function initApp() {
      switchSystem(activeSystem);
      calculateStats();

      const searchInput = document.getElementById('searchInput');
      searchInput.addEventListener('input', (e) => {
        searchQuery = e.target.value;
        renderTree();
      });

      document.addEventListener('keydown', (e) => {
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
          e.preventDefault();
          searchInput.focus();
        } else if (e.key === '/') {
          if (document.activeElement !== searchInput) {
            e.preventDefault();
            searchInput.focus();
          }
        } else if (e.key === 'Escape') {
          closeDrawer();
          if (document.activeElement === searchInput) {
            searchInput.blur();
          }
          searchInput.value = '';
          searchQuery = '';
          renderTree();
        }
      });
    }

    function calculateStats() {
      let cefrPoints = 0;
      Object.values(CEFR_DB.levels).forEach(l => {
        l.categories.forEach(c => {
          c.subs.forEach(s => {
            cefrPoints += s.points.length;
          });
        });
      });

      let amPoints = 0;
      Object.values(AMERICAN_DB.levels).forEach(l => {
        l.categories.forEach(c => {
          c.subs.forEach(s => {
            amPoints += s.points.length;
          });
        });
      });

      let discCount = 0;
      DISCREPANCIES_DB.categories.forEach(c => {
        discCount += c.items.length;
      });

      document.getElementById('statCefr').textContent = cefrPoints;
      document.getElementById('statAmerican').textContent = amPoints;
      document.getElementById('statDisc').textContent = discCount;

      const grandTotal = cefrPoints + amPoints + discCount;
      document.getElementById('statTotal').textContent = grandTotal;

      // Progress bar percentage
      const totalCombined = cefrPoints + amPoints;
      const progressPercent = totalCombined > 0 ? Math.round((cefrPoints / totalCombined) * 100) : 50;
      document.getElementById('statProgressFill').style.width = progressPercent + '%';
    }

    function switchSystem(system) {
      activeSystem = system;
      activeLevelFilter = 'all';
      searchQuery = '';
      document.getElementById('searchInput').value = '';
      
      document.querySelectorAll('.tab-btn').forEach(btn => {
        if (btn.dataset.sys === system) {
          btn.classList.add('active');
        } else {
          btn.classList.remove('active');
        }
      });

      const levelGrid = document.getElementById('levelSelectorGrid');
      const levelSelectorSection = document.getElementById('levelSelectorSection');
      const quickNavSection = document.getElementById('quickNavSection');

      if (system === 'Discrepancies') {
        levelSelectorSection.style.display = 'none';
        quickNavSection.style.display = 'none';
      } else {
        levelSelectorSection.style.display = 'flex';
        quickNavSection.style.display = 'flex';
        
        levelGrid.innerHTML = '<button class="level-btn active" onclick="setLevelFilter(\\'all\\', this)">ALL</button>';
        
        const db = system === 'CEFR' ? CEFR_DB : AMERICAN_DB;
        Object.keys(db.levels).forEach((lvlName, idx) => {
          const shortName = system === 'CEFR' ? lvlName.split(' - ')[0] : 'L' + (idx + 1);
          const btn = document.createElement('button');
          btn.className = 'level-btn';
          btn.style.setProperty('--level-color', getLevelColor(idx));
          btn.style.setProperty('--level-color-alpha', getLevelColorAlpha(idx, 0.25));
          btn.textContent = shortName;
          btn.onclick = () => setLevelFilter(lvlName, btn);
          levelGrid.appendChild(btn);
        });
      }

      // Pre-expand top levels
      expandedPaths.clear();
      const db = system === 'CEFR' ? CEFR_DB : (system === 'American' ? AMERICAN_DB : null);
      if (db) {
        Object.keys(db.levels).forEach(lvlName => {
          expandedPaths.add(`${system}/${lvlName}`);
        });
      }

      renderTree();
    }

    function setLevelFilter(levelName, btn) {
      activeLevelFilter = levelName;
      document.querySelectorAll('.level-btn').forEach(b => {
        b.classList.remove('active');
        for (let i = 0; i < 6; i++) {
          b.classList.remove(`active-cefr-${i}`);
        }
      });
      
      btn.classList.add('active');
      if (levelName !== 'all') {
        const btns = Array.from(document.getElementById('levelSelectorGrid').querySelectorAll('.level-btn'));
        const index = btns.indexOf(btn) - 1; // subtract ALL button
        btn.classList.add(`active-cefr-${index % 6}`);
      }
      renderTree();
    }

    function jumpToCategory(term) {
      document.getElementById('searchInput').value = term;
      searchQuery = term;
      
      // Auto expand matches
      const db = activeSystem === 'CEFR' ? CEFR_DB : (activeSystem === 'American' ? AMERICAN_DB : null);
      if (db) {
        Object.entries(db.levels).forEach(([lvlName, lvlData]) => {
          lvlData.categories.forEach(cat => {
            if (cat.category.toLowerCase().includes(term.toLowerCase())) {
              expandedPaths.add(`${activeSystem}/${lvlName}`);
              expandedPaths.add(`${activeSystem}/${lvlName}/${cat.category}`);
            }
          });
        });
      }
      
      renderTree();
    }

    function togglePath(path) {
      if (expandedPaths.has(path)) {
        expandedPaths.delete(path);
      } else {
        expandedPaths.add(path);
      }
      renderTree();
    }

    function expandAll() {
      const db = activeSystem === 'CEFR' ? CEFR_DB : (activeSystem === 'American' ? AMERICAN_DB : null);
      if (db) {
        Object.entries(db.levels).forEach(([lvlName, lvlData]) => {
          expandedPaths.add(`${activeSystem}/${lvlName}`);
          lvlData.categories.forEach(cat => {
            expandedPaths.add(`${activeSystem}/${lvlName}/${cat.category}`);
            cat.subs.forEach(sub => {
              expandedPaths.add(`${activeSystem}/${lvlName}/${cat.category}/${sub.subcategory}`);
            });
          });
        });
      } else if (activeSystem === 'Discrepancies') {
        DISCREPANCIES_DB.categories.forEach(cat => {
          expandedPaths.add(`${activeSystem}/${cat.name}`);
        });
      }
      renderTree();
    }

    function collapseAll() {
      expandedPaths.clear();
      renderTree();
    }

    // Renderer of database tree
    function renderTree() {
      const treeContainer = document.getElementById('treeContainer');
      treeContainer.innerHTML = '';

      if (activeSystem === 'Discrepancies') {
        renderDiscrepancies();
        return;
      }

      const db = activeSystem === 'CEFR' ? CEFR_DB : AMERICAN_DB;
      let totalMatchCount = 0;
      const query = searchQuery.toLowerCase().trim();

      Object.entries(db.levels).forEach(([lvlName, lvlData], lvlIdx) => {
        if (activeLevelFilter !== 'all' && lvlName !== activeLevelFilter) {
          return;
        }

        const lvlColor = getLevelColor(lvlIdx);
        const lvlColorAlpha = getLevelColorAlpha(lvlIdx, 0.03);
        const lvlColorAlphaBorder = getLevelColorAlpha(lvlIdx, 0.12);
        
        let lvlHtml = '';
        let levelPointsCount = 0;

        lvlData.categories.forEach((cat, catIdx) => {
          let catHtml = '';
          let catPointsCount = 0;

          cat.subs.forEach((sub, subIdx) => {
            let subHtml = '';
            let subPointsCount = 0;

            sub.points.forEach((pt) => {
              const matchesQuery = !query || pt.toLowerCase().includes(query) || 
                                   sub.subcategory.toLowerCase().includes(query) || 
                                   cat.category.toLowerCase().includes(query);
              if (matchesQuery) {
                subPointsCount++;
                
                let displayTxt = escapeHtml(pt);
                if (query) {
                  const escapedQuery = escapeRegExp(query);
                  const regex = new RegExp(`(${escapedQuery})`, 'gi');
                  displayTxt = displayTxt.replace(regex, '<span class="search-highlight">$1</span>');
                }
                
                // Format discrepancy tags
                displayTxt = displayTxt.replace(/#(BA-\\d{3})/g, (match, baId) => {
                  return `<span class="ba-tag" onclick="openDiscrepancy('${baId}', event)"><span class="flag-icon">🇬🇧/🇺🇸</span> ${baId}</span>`;
                });

                subHtml += `
                  <div class="point-node">
                    <span class="point-bullet">•</span>
                    <span class="point-text">${displayTxt}</span>
                  </div>
                `;
              }
            });

            if (subHtml) {
              catPointsCount += subPointsCount;
              const subPath = `${activeSystem}/${lvlName}/${cat.category}/${sub.subcategory}`;
              const isSubExpanded = expandedPaths.has(subPath) || query;

              catHtml += `
                <div class="sub-node">
                  <div class="sub-header" onclick="togglePath('${subPath}')">
                    <span class="chevron-icon ${isSubExpanded ? 'open' : ''}">▶</span>
                    <span class="sub-icon">📋</span>
                    <span class="sub-title">${escapeHtml(sub.subcategory)}</span>
                    <span class="tab-badge" style="margin-left: 8px; font-size: 9px; padding: 1px 4px;">${subPointsCount} pts</span>
                  </div>
                  <div class="sub-body ${isSubExpanded ? '' : 'collapsed'}">
                    ${subHtml}
                  </div>
                </div>
              `;
            }
          });

          if (catHtml) {
            levelPointsCount += catPointsCount;
            const catPath = `${activeSystem}/${lvlName}/${cat.category}`;
            const isCatExpanded = expandedPaths.has(catPath) || query;
            
            let catIcon = '📁';
            if (cat.category.includes('Irregular')) catIcon = '🔄';
            else if (cat.category.includes('Phrasal')) catIcon = '📝';
            else if (cat.category.includes('Syntax')) catIcon = '🔷';

            lvlHtml += `
              <div class="cat-node">
                <div class="cat-header" onclick="togglePath('${catPath}')">
                  <span class="chevron-icon ${isCatExpanded ? 'open' : ''}">▶</span>
                  <span class="cat-icon">${catIcon}</span>
                  <span class="cat-title">${escapeHtml(cat.category)}</span>
                  <span class="cat-count">${catPointsCount} pts</span>
                </div>
                <div class="cat-body ${isCatExpanded ? '' : 'collapsed'}">
                  ${catHtml}
                </div>
              </div>
            `;
          }
        });

        if (lvlHtml) {
          totalMatchCount += levelPointsCount;
          const lvlPath = `${activeSystem}/${lvlName}`;
          const isLvlExpanded = expandedPaths.has(lvlPath) || query;

          const card = document.createElement('div');
          card.className = 'level-card';
          card.style.setProperty('--level-color', lvlColor);
          card.style.setProperty('--level-color-alpha', lvlColorAlpha);
          card.style.setProperty('--level-color-alpha-border', lvlColorAlphaBorder);
          
          card.innerHTML = `
            <div class="level-header" onclick="togglePath('${lvlPath}')">
              <span class="chevron-icon ${isLvlExpanded ? 'open' : ''}">▶</span>
              <span class="level-icon">📊</span>
              <div class="level-title-wrapper">
                <span class="level-name">${escapeHtml(lvlName)}</span>
                <span class="level-desc">${escapeHtml(lvlData.description || '')}</span>
              </div>
              <span class="level-badge">${levelPointsCount} pts</span>
            </div>
            <div class="level-body ${isLvlExpanded ? '' : 'collapsed'}">
              ${lvlHtml}
            </div>
          `;
          treeContainer.appendChild(card);
        }
      });

      document.getElementById('resultsCount').textContent = `${totalMatchCount} results`;
      
      if (totalMatchCount === 0) {
        renderEmptyState();
      }
    }

    function renderDiscrepancies() {
      const treeContainer = document.getElementById('treeContainer');
      treeContainer.innerHTML = '';
      
      let totalMatchCount = 0;
      const query = searchQuery.toLowerCase().trim();

      DISCREPANCIES_DB.categories.forEach((cat) => {
        let catHtml = '';
        let catItemsCount = 0;

        cat.items.forEach(item => {
          const searchSpace = `${item.id} ${item.point} ${item.bre} ${item.ame} ${item.key_difference || ''}`.toLowerCase();
          const matchesQuery = !query || searchSpace.includes(query);
          
          if (matchesQuery) {
            catItemsCount++;
            totalMatchCount++;

            let ptText = escapeHtml(item.point);
            let breText = escapeHtml(item.bre);
            let ameText = escapeHtml(item.ame);

            if (query) {
              const regex = new RegExp(`(${escapeRegExp(query)})`, 'gi');
              ptText = ptText.replace(regex, '<span class="search-highlight">$1</span>');
              breText = breText.replace(regex, '<span class="search-highlight">$1</span>');
              ameText = ameText.replace(regex, '<span class="search-highlight">$1</span>');
            }

            catHtml += `
              <div class="point-node" style="flex-direction: column; align-items: stretch; border: 1px solid var(--border-color); background-color: rgba(255, 255, 255, 0.01); border-radius: 12px; padding: 16px; margin: 8px 0; cursor: pointer; transition: all var(--transition-fast);" onclick="openDiscrepancy('${item.id}', event)">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                  <span style="font-family: var(--font-headings); font-size: 11px; font-weight: 800; color: var(--accent-rose); background-color: rgba(244, 63, 94, 0.12); padding: 2px 8px; border-radius: 4px; border: 1px solid rgba(244, 63, 94, 0.2);">${item.id}</span>
                  <span style="font-family: var(--font-headings); font-size: 13px; font-weight: 700; color: #fff;">${ptText}</span>
                </div>
                
                <div style="display: flex; flex-direction: column; gap: 6px; margin-left: 4px; border-left: 2px solid rgba(255, 255, 255, 0.05); padding-left: 12px; margin-bottom: 6px;">
                  <div style="font-size: 12px; line-height: 1.5; color: var(--text-secondary);"><strong style="color: var(--accent-primary);">🇬🇧 BrE:</strong> ${breText}</div>
                  <div style="font-size: 12px; line-height: 1.5; color: var(--text-secondary);"><strong style="color: var(--accent-orange);">🇺🇸 AmE:</strong> ${ameText}</div>
                </div>

                <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.03); padding-top: 8px; margin-top: 4px; font-size: 9.5px; color: var(--text-muted);">
                  <span>Reference: CEFR: ${item.cefr_level || 'N/A'} · American: ${item.american_level || 'N/A'}</span>
                  <span style="color: var(--accent-rose); font-weight:600;">View Details &rarr;</span>
                </div>
              </div>
            `;
          }
        });

        if (catHtml) {
          const catPath = `${activeSystem}/${cat.name}`;
          const isCatExpanded = expandedPaths.has(catPath) || query;

          const card = document.createElement('div');
          card.className = 'level-card';
          card.style.setProperty('--level-color', '#f43f5e');
          card.style.setProperty('--level-color-alpha', 'rgba(244, 63, 94, 0.02)');
          card.style.setProperty('--level-color-alpha-border', 'rgba(244, 63, 94, 0.15)');

          card.innerHTML = `
            <div class="level-header" onclick="togglePath('${catPath}')">
              <span class="chevron-icon ${isCatExpanded ? 'open' : ''}">▶</span>
              <span class="level-icon">🔬</span>
              <div class="level-title-wrapper">
                <span class="level-name">${escapeHtml(cat.name)}</span>
                <span class="level-desc">${escapeHtml(cat.description || 'Divergences between British and American grammatical usage')}</span>
              </div>
              <span class="level-badge" style="background-color: rgba(244, 63, 94, 0.12); color: #fda4af; border-color: rgba(244, 63, 94, 0.2);">${catItemsCount} items</span>
            </div>
            <div class="level-body ${isCatExpanded ? '' : 'collapsed'}" style="padding: 10px 20px;">
              ${catHtml}
            </div>
          `;
          treeContainer.appendChild(card);
        }
      });

      document.getElementById('resultsCount').textContent = `${totalMatchCount} results`;

      if (totalMatchCount === 0) {
        renderEmptyState();
      }
    }

    function renderEmptyState() {
      const treeContainer = document.getElementById('treeContainer');
      treeContainer.innerHTML = `
        <div style="padding: 60px; text-align: center; color: var(--text-secondary);">
          <div style="font-size: 40px; margin-bottom: 16px;">🔍</div>
          <div style="font-family: var(--font-headings); font-size: 16px; font-weight: 700; color: #fff; margin-bottom: 8px;">No results found</div>
          <div style="font-size: 13px;">No entries matched your search query "${escapeHtml(searchQuery)}"</div>
        </div>
      `;
    }

    // Side Drawer control
    function openDiscrepancy(baId, event) {
      if (event) {
        event.stopPropagation();
      }

      let foundItem = null;
      for (const cat of DISCREPANCIES_DB.categories) {
        for (const item of cat.items) {
          if (item.id === baId) {
            foundItem = item;
            break;
          }
        }
        if (foundItem) break;
      }

      if (!foundItem) return;

      document.getElementById('drawerBadge').textContent = foundItem.id;
      document.getElementById('drawerTitle').textContent = foundItem.point;
      document.getElementById('breContent').textContent = foundItem.bre;
      document.getElementById('ameContent').textContent = foundItem.ame;

      const examplesContainer = document.getElementById('examplesContainer');
      examplesContainer.innerHTML = '';
      if (foundItem.example_pair && foundItem.example_pair.length > 0) {
        foundItem.example_pair.forEach(ex => {
          const line = document.createElement('div');
          line.className = 'ex-line';
          line.textContent = ex;
          examplesContainer.appendChild(line);
        });
      } else {
        examplesContainer.innerHTML = '<div style="color: var(--text-muted);">No examples available</div>';
      }

      const keyDiffSection = document.getElementById('keyDiffSection');
      if (foundItem.key_difference) {
        keyDiffSection.style.display = 'block';
        document.getElementById('keyDiffContent').textContent = foundItem.key_difference;
      } else {
        keyDiffSection.style.display = 'none';
      }

      document.getElementById('metaLevels').textContent = `CEFR Mapping: ${foundItem.cefr_level || 'N/A'}  ·  American Mapping: ${foundItem.american_level || 'N/A'}`;

      document.getElementById('discrepancyDrawer').classList.add('open');
      document.getElementById('drawerBackdrop').classList.add('active');
    }

    function closeDrawer() {
      document.getElementById('discrepancyDrawer').classList.remove('open');
      document.getElementById('drawerBackdrop').classList.remove('active');
    }

    function copyDiscrepancyToClipboard() {
      const baId = document.getElementById('drawerBadge').textContent;
      const title = document.getElementById('drawerTitle').textContent;
      const bre = document.getElementById('breContent').textContent;
      const ame = document.getElementById('ameContent').textContent;
      const examples = Array.from(document.getElementById('examplesContainer').querySelectorAll('.ex-line')).map(el => el.textContent).join('\\n');
      const kd = document.getElementById('keyDiffContent').textContent;

      const text = `Comparative Grammar: ${baId} - ${title}\\n\\n🇬🇧 British English (BrE):\\n${bre}\\n\\n🇺🇸 American English (AmE):\\n${ame}\\n\\nExamples:\\n${examples}\\n\\nKey Difference:\\n${kd}`;

      navigator.clipboard.writeText(text).then(() => {
        const copyBtn = document.getElementById('drawerCopyBtn');
        const origContent = copyBtn.innerHTML;
        copyBtn.innerHTML = '✓ Copied';
        setTimeout(() => {
          copyBtn.innerHTML = origContent;
        }, 2000);
      }).catch(err => {
        console.error('Failed to copy text: ', err);
      });
    }

    // Boot
    window.onload = initApp;
  </script>
</body>
</html>
"""

# Replace placeholders
html_content = html_template
html_content = html_content.replace("{{CEFR_DATA}}", cefr_js)
html_content = html_content.replace("{{AMERICAN_DATA}}", am_js)
html_content = html_content.replace("{{DISCREPANCIES_DATA}}", disc_js)
html_content = html_content.replace("{{CEFR_COUNT}}", str(cefr_gr))
html_content = html_content.replace("{{AME_COUNT}}", str(ame_gr))
html_content = html_content.replace("{{DISC_COUNT}}", str(disc_total))

# Save to index.html and pre-rendered.html
with open(INDEX_OUT, "w", encoding="utf-8") as f:
    f.write(html_content)

with open(PRERENDER_OUT, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ Viewer successfully updated:")
print(f"   Saved to {INDEX_OUT} ({len(html_content)} bytes)")
print(f"   Saved to {PRERENDER_OUT} ({len(html_content)} bytes)")
print(f"   CEFR points: {cefr_gr} · American points: {ame_gr} · Discrepancies: {disc_total}")
