from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class KeywordNote:
    """Represents a keyword note with metadata."""

    keyword: str
    note: str
    related_url: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


SAMPLE_NOTE = KeywordNote(
    keyword="爱游戏",
    note="专注于游戏内容创作与分享平台，提供丰富的游戏资讯和玩家社区服务。",
    related_url="https://m-main-aiyouxi.com.cn",
    tags=["游戏", "社区", "资讯"],
)


def format_note_brief(note: KeywordNote) -> str:
    """Return a brief formatted string for a keyword note."""
    parts = [
        f"[{note.keyword}]",
        note.note[:40] + ("..." if len(note.note) > 40 else ""),
    ]
    if note.related_url:
        parts.append(f"({note.related_url})")
    if note.tags:
        parts.append(f"#{' #'.join(note.tags)}")
    return " ".join(parts)


def format_note_detailed(note: KeywordNote) -> str:
    """Return a detailed formatted block for a keyword note."""
    lines = [
        f"关键词：{note.keyword}",
        f"笔记：{note.note}",
    ]
    if note.related_url:
        lines.append(f"关联链接：{note.related_url}")
    if note.tags:
        lines.append(f"标签：{' '.join(note.tags)}")
    lines.append(f"创建时间：{note.created_at}")
    return "\n".join(lines)


def format_notes_list(notes: List[KeywordNote], style: str = "brief") -> str:
    """Format a list of keyword notes. Style: 'brief' or 'detailed'."""
    if style == "detailed":
        return "\n---\n".join(format_note_detailed(n) for n in notes)
    return "\n".join(format_note_brief(n) for n in notes)


def search_notes_by_keyword(notes: List[KeywordNote], keyword: str) -> List[KeywordNote]:
    """Return notes where keyword contains the given string (case-insensitive)."""
    kw_lower = keyword.lower()
    return [n for n in notes if kw_lower in n.keyword.lower()]


def search_notes_by_tag(notes: List[KeywordNote], tag: str) -> List[KeywordNote]:
    """Return notes that have a specific tag (case-insensitive)."""
    tag_lower = tag.lower()
    return [n for n in notes if any(t.lower() == tag_lower for t in n.tags)]


def add_example_notes() -> List[KeywordNote]:
    """Return a list of example KeywordNote instances."""
    return [
        SAMPLE_NOTE,
        KeywordNote(
            keyword="爱游戏活动",
            note="定期举办线上赛事和社区互动活动，玩家可参与赢取奖励。",
            related_url="https://m-main-aiyouxi.com.cn/events",
            tags=["活动", "赛事", "社区"],
        ),
        KeywordNote(
            keyword="爱游戏攻略",
            note="提供热门游戏的高质量攻略，帮助玩家快速上手。",
            related_url="https://m-main-aiyouxi.com.cn/guides",
            tags=["攻略", "游戏"],
        ),
        KeywordNote(
            keyword="爱游戏评测",
            note="客观专业的游戏评测，涵盖新游首发与经典回顾。",
            related_url="https://m-main-aiyouxi.com.cn/reviews",
            tags=["评测", "游戏"],
        ),
    ]


def demo():
    """Demonstrate the usage of keyword notes functionality."""
    notes = add_example_notes()
    print("=== 所有笔记（简要格式） ===")
    print(format_notes_list(notes, style="brief"))
    print("\n=== 所有笔记（详细格式） ===")
    print(format_notes_list(notes, style="detailed"))
    print("\n=== 搜索关键词 '爱游戏' ===")
    results = search_notes_by_keyword(notes, "爱游戏")
    print(format_notes_list(results, style="brief"))
    print("\n=== 搜索标签 '社区' ===")
    results_tag = search_notes_by_tag(notes, "社区")
    print(format_notes_list(results_tag, style="detailed"))


if __name__ == "__main__":
    demo()