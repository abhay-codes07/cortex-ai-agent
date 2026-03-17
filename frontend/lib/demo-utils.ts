import type { TimelineEvent } from './types';

export function extractTimelineFromDemoResult(result: Record<string, unknown>): TimelineEvent[] {
  const maybeTimeline = result.timeline;
  if (Array.isArray(maybeTimeline)) return maybeTimeline as TimelineEvent[];

  const maybeNested = result.result as { timeline?: unknown } | undefined;
  if (maybeNested && Array.isArray(maybeNested.timeline)) {
    return maybeNested.timeline as TimelineEvent[];
  }

  return [];
}
