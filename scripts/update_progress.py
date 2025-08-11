#!/usr/bin/env python3
"""
Progress Update Script for 90-Day SRE Journey

This script automatically calculates progress based on completed tasks
and updates the README.md file with current progress percentages.
"""

import re
import os
from datetime import datetime, timedelta
from typing import Tuple, List, Dict

class ProgressUpdater:
    def __init__(self, readme_path: str):
        self.readme_path = readme_path
        self.start_date = datetime(2025, 8, 11)  # August 11, 2025
        self.total_days = 90
        
    def read_readme(self) -> str:
        """Read the current README content."""
        with open(self.readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def write_readme(self, content: str) -> None:
        """Write updated content to README."""
        with open(self.readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def calculate_days_elapsed(self) -> int:
        """Calculate how many days have elapsed since start date."""
        today = datetime.now().date()
        start = self.start_date.date()
        
        if today < start:
            return 0
        
        elapsed = (today - start).days + 1  # +1 to include start day
        return min(elapsed, self.total_days)
    
    def count_completed_tasks(self, content: str) -> Dict[str, int]:
        """Count completed tasks by category."""
        # Count weekly tasks (main checklist items)
        weekly_pattern = r'- \[x\]'
        weekly_completed = len(re.findall(weekly_pattern, content))
        
        # Count deliverables
        deliverable_pattern = r'- \[x\].*?(?:Blog|GitHub|presentation|runbook|dashboard|toolkit|report|demo|guide|pipeline|framework|platform)'
        deliverable_completed = len(re.findall(deliverable_pattern, content, re.IGNORECASE))
        
        # Count skills acquired
        skills_section = re.search(r'### Skills Acquired\n(.*?)\n---', content, re.DOTALL)
        skills_completed = 0
        if skills_section:
            skills_text = skills_section.group(1)
            skills_completed = len(re.findall(r'- \[x\]', skills_text))
        
        # Estimate total tasks (you can adjust these numbers)
        total_weekly_tasks = 48  # 12 weeks * 4 tasks per week
        total_deliverables = 36  # 12 weeks * 3 deliverables per week
        total_skills = 9  # From the skills list
        
        return {
            'weekly_completed': weekly_completed,
            'weekly_total': total_weekly_tasks,
            'deliverable_completed': deliverable_completed,
            'deliverable_total': total_deliverables,
            'skills_completed': skills_completed,
            'skills_total': total_skills
        }
    
    def calculate_phase_progress(self, content: str) -> Dict[str, Dict[str, int]]:
        """Calculate progress for each phase."""
        phases = {
            'Foundation': {'weeks': [1, 2, 3, 4], 'completed': 0},
            'Technical': {'weeks': [5, 6, 7, 8], 'completed': 0},
            'Production': {'weeks': [9, 10, 11, 12], 'completed': 0}
        }
        
        # Count completed tasks per week
        for phase, data in phases.items():
            completed = 0
            for week_num in data['weeks']:
                week_pattern = rf'### Week {week_num}:.*?\n(.*?)(?=### Week|\n## |$)'
                week_match = re.search(week_pattern, content, re.DOTALL)
                if week_match:
                    week_content = week_match.group(1)
                    week_completed = len(re.findall(r'- \[x\]', week_content))
                    completed += week_completed
            
            # Each phase has roughly 16 tasks (4 weeks * 4 tasks per week)
            phases[phase]['completed'] = min(int((completed / 16) * 100), 100)
        
        return phases
    
    def update_progress_badge(self, content: str, overall_percentage: int) -> str:
        """Update the progress badge with current percentage."""
        # Determine badge color based on progress
        if overall_percentage < 25:
            color = 'red'
        elif overall_percentage < 50:
            color = 'yellow'
        elif overall_percentage < 75:
            color = 'orange'
        else:
            color = 'brightgreen'
        
        old_badge = r'!\[Progress\]\(https://img\.shields\.io/badge/Progress-\d+%25-\w+\)'
        new_badge = f'![Progress](https://img.shields.io/badge/Progress-{overall_percentage}%25-{color})'
        
        return re.sub(old_badge, new_badge, content)
    
    def update_overall_progress(self, content: str, days_elapsed: int, overall_percentage: int) -> str:
        """Update the overall progress section."""
        old_pattern = r'### Overall Progress: \d+/90 days \(\d+%\)'
        new_text = f'### Overall Progress: {days_elapsed}/90 days ({overall_percentage}%)'
        
        return re.sub(old_pattern, new_text, content)
    
    def update_phase_progress_bars(self, content: str, phases: Dict[str, Dict[str, int]]) -> str:
        """Update the phase progress bars."""
        for phase_name, data in phases.items():
            percentage = data['completed']
            filled_blocks = percentage // 10
            empty_blocks = 10 - filled_blocks
            
            progress_bar = '⬛' * filled_blocks + '⬜' * empty_blocks
            
            old_pattern = rf'{phase_name}:\s+[⬜⬛]+\s+\d+%'
            new_text = f'{phase_name}:     {progress_bar} {percentage}%'
            
            content = re.sub(old_pattern, new_text, content)
        
        return content
    
    def calculate_overall_progress(self, tasks: Dict, days_elapsed: int) -> int:
        """Calculate overall progress percentage."""
        # Weight different components
        task_weight = 0.6  # 60% based on completed tasks
        time_weight = 0.4  # 40% based on elapsed time
        
        # Calculate task completion percentage
        total_completed = (
            tasks['weekly_completed'] + 
            tasks['deliverable_completed'] + 
            tasks['skills_completed']
        )
        total_tasks = (
            tasks['weekly_total'] + 
            tasks['deliverable_total'] + 
            tasks['skills_total']
        )
        
        task_percentage = (total_completed / total_tasks) * 100 if total_tasks > 0 else 0
        time_percentage = (days_elapsed / self.total_days) * 100
        
        # Weighted average
        overall_percentage = int((task_percentage * task_weight) + (time_percentage * time_weight))
        return min(overall_percentage, 100)
    
    def update_status_badge(self, content: str, days_elapsed: int) -> str:
        """Update status badge based on current progress."""
        if days_elapsed == 0:
            status = "Starting%20Aug%2011"
            color = "green"
        elif days_elapsed <= 30:
            status = f"Day%20{days_elapsed}%20-%20Foundation"
            color = "yellow"
        elif days_elapsed <= 60:
            status = f"Day%20{days_elapsed}%20-%20Technical"
            color = "orange"
        elif days_elapsed < 90:
            status = f"Day%20{days_elapsed}%20-%20Production"
            color = "red"
        else:
            status = "Completed!"
            color = "brightgreen"
        
        old_pattern = r'!\[Status\]\(https://img\.shields\.io/badge/Status-[^)]+\)'
        new_badge = f'![Status](https://img.shields.io/badge/Status-{status}-{color})'
        
        return re.sub(old_pattern, new_badge, content)
    
    def update_progress(self) -> None:
        """Main method to update all progress indicators."""
        print("🔄 Updating 90-Day SRE Journey progress...")
        
        # Read current README
        content = self.read_readme()
        
        # Calculate progress
        days_elapsed = self.calculate_days_elapsed()
        tasks = self.count_completed_tasks(content)
        phases = self.calculate_phase_progress(content)
        overall_percentage = self.calculate_overall_progress(tasks, days_elapsed)
        
        # Update content
        content = self.update_progress_badge(content, overall_percentage)
        content = self.update_status_badge(content, days_elapsed)
        content = self.update_overall_progress(content, days_elapsed, overall_percentage)
        content = self.update_phase_progress_bars(content, phases)
        
        # Write updated README
        self.write_readme(content)
        
        # Print summary
        print(f"✅ Progress updated successfully!")
        print(f"   📅 Days elapsed: {days_elapsed}/90")
        print(f"   📊 Overall progress: {overall_percentage}%")
        print(f"   📋 Completed tasks: {tasks['weekly_completed']}/{tasks['weekly_total']} weekly")
        print(f"   📦 Completed deliverables: {tasks['deliverable_completed']}/{tasks['deliverable_total']}")
        print(f"   🎯 Skills acquired: {tasks['skills_completed']}/{tasks['skills_total']}")
        print(f"   🏗️  Phase progress:")
        for phase, data in phases.items():
            print(f"      {phase}: {data['completed']}%")

def main():
    """Main execution function."""
    # Get the README path relative to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    readme_path = os.path.join(os.path.dirname(script_dir), 'README.md')
    
    if not os.path.exists(readme_path):
        print(f"❌ Error: README.md not found at {readme_path}")
        return
    
    updater = ProgressUpdater(readme_path)
    updater.update_progress()

if __name__ == "__main__":
    main()
