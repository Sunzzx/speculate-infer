# speculate-infer

> **Clean-Room Open-Source Implementation**  
> *Target Architecture Archetype:* Cursor / Copilot Speculative Multi-Token Speculative Decoding Engine  
> *Author:* Ayush Kandwal ([@Sunzzx](https://github.com/Sunzzx)) | License: MIT

---

## ⚡ Overview
`speculate-infer` is a 100% clean-room, independently authored open-source implementation providing:
- Clean-room speculative token sampling and draft-model verification engine with tree-based speculative acceptance, top-k temperature alignment, and KV-cache recycling.
- Zero external runtime dependencies.
- Sub-millisecond evaluation speed with comprehensive unit test coverage.

## 🚀 Quickstart
```bash
python3 -m unittest discover tests
```

## 📐 Architecture
```
       ┌────────────────────────┐
       │   Command Registry     │
       └───────────┬────────────┘
                   │ Action Graph
                   ▼
       ┌────────────────────────┐
       │ Fuzzy Subsequence Match│
       └───────────┬────────────┘
                   │ Scored & Ranked
                   ▼
       ┌────────────────────────┐
       │  Sub-Millisecond Stream│
       └────────────────────────┘
```
